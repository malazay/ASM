from django.shortcuts import render, get_object_or_404
from ASM.appium.manager import start_appium_server, stop_appium_server
from ASM.monitor.stats import percore_cpu
import time

# Create your views here.
from django.http import HttpResponseRedirect
from .models import Server


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
    reset = "no"
    if server.full_reset:
        reset = "full"
    start_appium_server(server.ip_address, server.port_number, server.chromedriver_port, server.bootstrap_port,
                        server.selendroid_port, reset, server.session_override, "--local-timezone", server_id+".txt")
    time.sleep(5)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def monitor(request):
    cpu_count = percore_cpu()
    server_list = Server.objects.all()
    context = {'server_list': server_list, 'cpu_count': cpu_count}
    return render(request, 'dashboard/monitor.html', context)
