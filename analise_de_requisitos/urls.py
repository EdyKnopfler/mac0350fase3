from django.conf.urls import url
from django.contrib import admin

from analise_de_requisitos import views

urlpatterns = [
    url(r'^index/$', views.index, name='ar_index'),
    url(r'^show/(?P<ar_id>\d+)$', views.show, name='ar_show'),
    url(r'^new/$', views.new, name='ar_new'),
    url(r'^create/$', views.create, name='ar_create'),
    url(r'^edit/$', views.edit, name='ar_edit'),
    url(r'^update/$', views.update, name='ar_update'),
    url(r'^delete/$', views.delete, name='ar_delete')
]
