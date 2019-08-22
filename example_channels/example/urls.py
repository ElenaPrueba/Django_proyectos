from django.conf.urls import url
from example.views import user_list

app_name='example'

urlpatterns = [
    url(r'^$', user_list, name='user_list'),
]
