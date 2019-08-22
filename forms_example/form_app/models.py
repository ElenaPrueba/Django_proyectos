from django.db import models
from django.conf import settings
from django.db.models import Q
from django.utils import timezone
#from __future__ import unicode_literals

# Create your models here.
User = settings.AUTH_USER_MODEL

def upload_location(instance, filename):
    PostModel= instance.__class__
    new_id= PostModel.objects.order_by("id").last().id+1
    return ("%s/%s")%(new_id, filename)


class Post(models.Model): # blogpost_set -> queryset
    # id = models.IntegerField() # pk
    user    = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    #user    = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.SET_NULL)
    #image   = models.ImageField(upload_to='image/', blank=True, null=True)
    #image   = models.FileField(upload_to=upload_location, blank=True, null=True)
    title  = models.CharField(max_length=120)
    slug   = models.SlugField(unique=True) # hello world -> hello-world
    content  = models.TextField(null=True, blank=True)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    draft= models.BooleanField(default=False)
    publish = models.DateTimeField(auto_now=False, auto_now_add=False)#, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    #objects = BlogPostManager()
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish', '-updated', '-timestamp']

    # def get_absolute_url(self):
    #     return f"/blog/{self.slug}"
    #
    # def get_edit_url(self):
    #     return f"{self.get_absolute_url()}/edit"
    #
    # def get_delete_url(self):
    #     return f"{self.get_absolute_url()}/delete"
