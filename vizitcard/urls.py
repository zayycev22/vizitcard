"""vizitcard URL Configuration

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
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('', index),
    path('register', register),
    path('login', login_view),
    path('logout', logout_view),
    path('activate/<str:token>', activate_user),
    path('profile', profile),
    path('profile/<str:username>', profile),
    path('forgot_password', forgot_password),
    path('forgot_password/<str:token>', new_password),
    path('change_profile', change_profile),
    path('organizations', organizations),
    path('enter_organization', enter_organization),
    path('request_create_organization', request_create_organization),
    path('activate_organization', activate_organization),
    path('delete_organization', delete_organization),
    path('create_card', create_card),
    path('new_card', new_card),
    path('admin', admin)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
