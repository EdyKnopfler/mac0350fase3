from django.conf.urls import url
from django.contrib import admin
from atividade import views

urlpatterns = [
    url(r'^show/(?P<atividade_id>\d+)$', views.show, name='atividade_show'),
    url(r'^new/$', views.new, name='atividade_new'),
    url(r'^create/$', views.create, name='atividade_create'),
    url(r'^edit/$', views.edit, name='atividade_edit'),
    url(r'^update/$', views.update, name='atividade_update'),
    url(r'^delete/$', views.delete, name='atividade_delete')
]
