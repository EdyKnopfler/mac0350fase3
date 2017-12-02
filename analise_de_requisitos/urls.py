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
    url(r'^delete/$', views.delete, name='ar_delete'),
    url(r'^remove_dev/(?P<dev_id>\d+)$', views.remove_dev, name='ar_remove_dev'),
    url(r'^select_dev/$', views.select_dev, name='ar_select_dev'),
    url(r'^add_dev/(?P<dev_id>\d+)$', views.add_dev, name='ar_add_dev')
]
