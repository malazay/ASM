__author__ = 'malazay'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<server_id>[0-9]+)/$', views.server_details, name='detail'), ####NO EXISTE SERVER_ID
]