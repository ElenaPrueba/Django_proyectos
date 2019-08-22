from django.urls import path, re_path

from .views import post_model_list_view, post_model_detail_view, post_model_create_view, post_model_update_view, post_model_delete_view, user_login, redirigir

from . import views

app_name='aplicacion'

urlpatterns = [
    path('', post_model_list_view, name = 'list'),# si la url fuera 'abc', en el navegador habria que añadir abc despúes de "aplicacion/"
    #path('login/', user_login, name = 'ulogin'),
    #path('login/','django.contrib.auth.views.login', {'template_name': '/login.html'}),
    #path('accounts/login/', auth_views.login),
    path('login/', user_login, name='ulogin'),
    path('create/', post_model_create_view, name = 'create'),
    path('post:<id>/', post_model_detail_view, name = 'detail'),
    path('post:<id>/delete/', post_model_delete_view, name = 'delete'),
    path('post:<id>/edit/', post_model_update_view, name = 'update'),
    re_path(r'^.', redirigir, name="redirig")

]
