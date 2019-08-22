"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import home, redirect_somewhere
from aplicacion.views import post_model_list_view

from django.conf.urls import handler404, handler500
from aplicacion import views as myapp_views
#from aplicacion.views import post_model_list-public_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('redirect/', redirect_somewhere, name = 'redirect_somewhere'),
    #path('login/', include('django.contrib.auth.views.login')),
    path('aplicacion/', include('django.contrib.auth.urls')),
    path('aplicacion/', include('aplicacion.urls',namespace='aplicacion')),#nuestra aplicacion controla todas las urls
    path('',include('aplicacion.urls'))

]
handler404 = myapp_views.handler404
handler500 = myapp_views.handler500

# handler404 = 'mysite.views.my_custom_page_not_found_view'
# handler500 = 'mysite.views.my_custom_error_view'
# handler403 = 'mysite.views.my_custom_permission_denied_view'
# handler400 = 'mysite.views.my_custom_bad_request_view'
