from django.conf.urls import url
from django.contrib import admin

from analise_de_requisitos import views

urlpatterns = [
    url(r'^index/$', views.index, name='ar_index')
]
