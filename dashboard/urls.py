__author__ = 'malazay'
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /dashboard/5/
    url(r'^(?P<server_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<server_id>[0-9]+)/stop/$', views.stop_server, name='stop'),
    url(r'^(?P<server_id>[0-9]+)/run/$', views.run_server, name='run'),
    url(r'^(?P<server_id>[0-9]+)/logs/$', views.log_viewer, name='logs'),
    url(r'^monitor/', views.monitor, name='monitor'),
]

