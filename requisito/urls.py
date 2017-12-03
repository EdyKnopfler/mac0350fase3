from django.conf.urls import url
from django.contrib import admin
from requisito import views

urlpatterns = [
    url(r'^show/(?P<requisito_id>\d+)$', views.show, name='requisito_show'),
    url(r'^new/$', views.new, name='requisito_new'),
    url(r'^create/$', views.create, name='requisito_create'),
    url(r'^edit/$', views.edit, name='requisito_edit'),
    url(r'^update/$', views.update, name='requisito_update'),
    url(r'^delete/$', views.delete, name='requisito_delete')
]
