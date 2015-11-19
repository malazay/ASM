__author__ = 'malazay'
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /dashboard/5/
    url(r'^(?P<server_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<server_id>[0-9]+)/stop/$', views.stop_server, name='stop'),
    url(r'^(?P<server_id>[0-9]+)/stop_webkit/$', views.stop_webkit, name='stop_webkit'),
    url(r'^(?P<server_id>[0-9]+)/run/$', views.run_server, name='run'),
    url(r'^(?P<server_id>[0-9]+)/run_webkit/$', views.start_webkit, name='run_webkit'),
    url(r'^(?P<server_id>[0-9]+)/logs/$', views.log_viewer, name='logs'),
    url(r'^(?P<server_id>[0-9]+)/webkit_logs/$', views.webkit_log_viewer, name='webkit_logs'),
    url(r'^(?P<server_id>[0-9]+)/stop_chromedriver/$', views.stop_chromedriver, name='stop_chromedriver'),
    url(r'^monitor/', views.monitor, name='monitor'),
    url(r'^monitor_data/', views.monitor_data, name='monitor_data'),
    url(r'^ajax/', views.ajax, name='ajaxdata'),
    url(r'^adb_json/', views.adb_devices_json, name='adb_devices_json'),
    url(r'^adb/', views.adb_devices, name='adb_devices'),
    url(r'^adb_reboot/(?P<device_name>[\w\-]+)', views.adb_reboot, name='adb_reboot'),

]

