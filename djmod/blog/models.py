from datetime import timedelta, datetime, date
from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.utils.timesince import timesince

# Create your models here.


from .validators import validate_author_email, validate_justin

PUBLISH_CHOICES = [
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private'),
]


class PostModelQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def post_title_items(self, value):
        return self.filter(title__icontains=value)



class PostModelManager(models.Manager):
    def get_queryset(self):
        return PostModelQuerySet(self.model, using=self._db)

    def all(self, *args, **kwargs):
        #qs = super(PostModelManager, self).all(*args, **kwargs).active()#filter(active=True)
        qs=self.get_queryset().active()
        return qs

    def get_timeframe(self, date1, date2):
        # Comprobar que son fechas
        # Comprueba que fecha1 es > fecha2
        qs=self.get_queryset()
        qs_time1= qs.filter(publish_date__gte=date1)
        qs_time2= qs_time1.filter(publish_date__lt=date2)
        #final_qs=(qs_time1 | qs_time2).distinct()
        return qs_time2#final_qs


class PostModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    active= models.BooleanField(default=True) #null=True puede ser vacío en la bbdd
    title = models.CharField(max_length=240,
                            verbose_name='Post title',
                            unique=True,
                            error_messages={                        # Mensajes de error
                                "unique": "Este titulo no es unico, intentalo otra vez",
                                "blank": "Este campo no esta completo, intentalo otra vez" #No hace nada
                                },
                                help_text="El titulo debe ser unico")
    slug = models.SlugField(null=True, blank=True) # useful for posts or blog posts
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    view_count = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email = models.EmailField(max_length=240, validators=[validate_justin], null=True, blank=True)
    updated=models.DateTimeField(auto_now=True) # last save
    timestamp=models.DateTimeField(auto_now_add=True) #Timestamp: cuándo fue creado, cuando lo ponemos en la bbdd
                                                    # auto_now_add: Se declara cuando se pone en la bbdd

    # PostModelManagers
    objects = PostModelManager()# Con esto, al hacer una query del estilo: PostModel.objects.all()
    other = PostModelManager()  # ó                                        PostModel.other.all()
                                # sobreescribimos el metodo "all" con la clase PostModelManager

    # def random_method(self, title,abc, edf, keyword=None):#title. abc, def son: args; keyword es: **kwargs
    #     print (title)
    #     print (keyword)

    def save(self, *args, **kwargs):
        # if not self.slug and self.title:
        #     self.slug=slugify(self.title)
        #print ("Hello there")
        #self.title='A new title' # No tiene sentido hacer esto, es mas, va a adar error xq hemos puesto al principio que el titulo tiene que ser unico
        super(PostModel, self).save(*args, **kwargs) # Cuando guarda imprime "Hello there"

    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'

    def __unicode__(self):
        return smart_text(self.title)

    def __str__(self):
        return smart_text(self.title)

    # def age(self):      #Instance Methods and properties
    #     now=timezone.now
    #     guess_age=timesince(self.publish_date)
    #     if str(guess_age) == "0 minutes":
    #         return "Unknown"
    #     return "{t} ago".format(t=guess_age)
    @property
    def age(self):
        if self.publish == 'publish':
            now=datetime.now()
            publish_time = datetime.combine(
                                    self.publish_date,
                                    datetime.now().min.time()
                        )
            try:
                difference= now -publish_time
            except:
                return "Unknown"
            if difference <= timedelta(minutes=1):
                return 'just now'
            return '{time} ago'.format(time=timesince(publish_time).split(', ')[0])
        return "Not published"

# Funciones fuera de la clase
# Señales
def blog_post_model_pre_save_receiver(sender, instance, *args, **kwargs):
    print("Antes de guardar")
    if not instance.slug and instance.title:
        instance.slug= slugify(instance.title)                  # El objeto se crea en esta funcion

pre_save.connect(blog_post_model_pre_save_receiver, sender=PostModel)


def blog_post_model_post_save_receiver(sender, instance, created, *args, **kwargs): # Despues de guardar envia los datos
    print("Despues de guardar")
    print(created)
    if created:
        if not instance.slug and instance.title:                                       # A partir de aqui trabaja con los datos
            instance.slug= slugify(instance.title)
            instance.save()

post_save.connect(blog_post_model_post_save_receiver, sender=PostModel) # Esto conecta el metodo de guardar del modelo con la señal, y despues se la manda al recibidor
