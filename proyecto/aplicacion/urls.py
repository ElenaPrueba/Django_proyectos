from django.urls import path, re_path, include

from .views import post_model_list_view, post_model_detail_view, post_model_create_view, post_model_update_view, post_model_delete_view, redirigir

from . import views

from django.views.generic import TemplateView

from django.contrib.auth import views as auth_views


from django.conf import settings
from django.conf.urls.static import static
app_name='aplicacion'

urlpatterns = [
    path('', post_model_list_view, name = 'list'),# si la url fuera 'abc', en el navegador habria que añadir abc despúes de "aplicacion/"

    #path('login/','django.contrib.auth.views.login', {'template_name': '/login.html'}),
    re_path(r'^login/$', auth_views.LoginView.as_view()),# auth_views.LoginView     .as_view()
    #path('accounts/login/', auth_views.LoginView.as_view()),

    path('create/', post_model_create_view, name = 'create'),

    path('post:<id>/', post_model_detail_view, name = 'detail'),
    path('post:<id>/delete/', post_model_delete_view, name = 'delete'),
    path('post:<id>/edit/', post_model_update_view, name = 'update'),

    re_path(r'^.', redirigir, name="redirig")

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
