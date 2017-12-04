"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from desenvolvedor import views

urlpatterns = [
    url(r'^$', views.index, name='desenvolvedor_index'),
    url(r'^enter/$', views.enter, name='desenvolvedor_enter'),
    url(r'^login/$', views.login, name='desenvolvedor_login'),
    url(r'^logout/$', views.logout, name='desenvolvedor_logout'),
    url(r'^new/$', views.new, name='desenvolvedor_new'),
    url(r'^create/$', views.create, name='desenvolvedor_create'),
    url(r'^edit/$', views.edit, name='desenvolvedor_edit'),
    url(r'^update/$', views.update, name='desenvolvedor_update'),
    url(r'^delete/$', views.delete, name='desenvolvedor_delete')
]
