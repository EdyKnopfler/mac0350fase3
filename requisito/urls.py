from django.conf.urls import url
from django.contrib import admin
from requisito import views

from requisito import views

urlpatterns = [
    url(r'^new/$', views.new, name='requisito_new'),
    url(r'^create/$', views.create, name='requisito_create')
]
