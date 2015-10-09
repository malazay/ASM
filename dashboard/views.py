from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from ASM.appium.manager import start_appium_server, stop_appium_server, adb, reboot, kill_chromedriver, adb_get_name
from ASM.monitor.stats import percore_cpu
import time

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from .models import Server
import collections
import json


def index(request):
    server_list = Server.objects.all()
    context = {'server_list': server_list}
    return render(request, 'dashboard/index.html', context)


def detail(request, server_id):
    server = get_object_or_404(Server, pk=server_id)
    server.server_status = server.isActive()
    return render(request, 'dashboard/detail.html', {'server': server})


def stop_server(request, server_id):
    server = get_object_or_404(Server, pk=server_id)
    server.server_status = server.isActive()
    try:
        stop_appium_server(server.port_number)
        time.sleep(2)
        pass
    except Exception as e:
        print "Error: " + e
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def log_viewer(request, server_id):
    server = get_object_or_404(Server, pk=server_id)
    return render(request, 'dashboard/log_viewer.html', {'server': server})


def run_server(request, server_id):
    server = get_object_or_404(Server, pk=server_id)
    server.server_status = server.isActive()
    params = "--local-timezone"
    reset = "no"
    if server.full_reset:
        reset = "full"
    if server.udid is not None and type(server.udid) is not 'NoneType' and len(server.udid) > 0:
        params += " -U " + server.udid
    start_appium_server(server.ip_address, server.port_number, server.chromedriver_port, server.bootstrap_port,
                        server.selendroid_port, reset, server.session_override, params, server_id+".txt")
    counter = 0
    while server.isActive() is not True and counter < 10:
        time.sleep(1)
        counter += 1
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@xframe_options_exempt
def monitor(request):
    cpu_count = percore_cpu()
    server_list = Server.objects.all()
    context = {'server_list': server_list, 'cpu_count': cpu_count}
    return render(request, 'dashboard/monitor.html', context)


def monitor_data(request):
    context = {'server_list': ""}
    return render(request, 'dashboard/monitor_data.html', context)


def ajax(request):
    data = collections.OrderedDict()
    cpu_count = percore_cpu()
    coredata = collections.OrderedDict()
    for core in cpu_count:
        coredata[core[0]] = core[1]
    data = coredata
    return HttpResponse(json.dumps(data), content_type="application/json")

def adb_devices_json(request):
    data = []
    for device in adb()[1:]:
        if len(device) > 0:
            data.append(device.split('\t'))
    return HttpResponse(json.dumps(data), content_type="application/json")

def adb_devices(request):
    data = []
    device_name = []
    for device in adb()[1:]:
        if len(device) > 0:
            data.append(device.split('\t'))
    context = {'devices': data, 'device_name': device_name}
    return render(request, 'dashboard/adb.html', context)

def adb_reboot(request, device_name):
    reboot(device_name)
    time.sleep(5)
    data = []
    status = []
    for device in adb()[1:]:
        if len(device) > 0:
            data.append(device.split('\t'))
    context = {'devices': data}
    return render(request, 'dashboard/adb.html', context)


def stop_chromedriver(request, server_id):
    server = get_object_or_404(Server, pk=server_id)
    try:
        kill_chromedriver(server.chromedriver_port)
        time.sleep(2)
        pass
    except Exception as e:
        print "Error: " + e
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
