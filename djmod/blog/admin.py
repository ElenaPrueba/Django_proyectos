from django.contrib import admin

# Register your models here.
from .models import PostModel

class PostModelAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'slug',
        'content',
        'publish',
        'publish_date',
        'active',
        'timestamp',
        'updated',
        'get_age'
    ]
    readonly_fields = ['updated', 'timestamp', 'get_age']

    def get_age(self, obj, *args, **kwargs): # Instance methods
        return str(obj.age)

    class Meta:
        model=PostModel

admin.site.register(PostModel, PostModelAdmin)
