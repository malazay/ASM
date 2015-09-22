from django.shortcuts import render, get_object_or_404
from ASM.appium.manager import start_appium_server, stop_appium_server
import time

# Create your views here.
from django.http import HttpResponse
from .models import Server


def index(request):
    server_list = Server.objects.all()

    context = {'server_list': server_list}
    return render(request, 'dashboard/index.html', context)


def detail(request, server_id):
    server = get_object_or_404(Server, pk=server_id)
    server.server_status = server.isActive()
    return render(request, 'dashboard/detail.html', {'server': server})


def server_status(request, server_id):
    server = get_object_or_404(Server, pk=server_id)
    server.server_status = server.isActive()
    start_appium_server(server.ip_address, server.port_number, server.chromedriver_port, server.bootstrap_port,
                        server.selendroid_port, "--no-reset --local-timezone")
    time.sleep(5)
    return render(request, 'dashboard/status.html', {'server': server})


def stop_server(request, server_id):
    server = get_object_or_404(Server, pk=server_id)
    server.server_status = server.isActive()
    try:
        stop_appium_server(server.port_number)
        time.sleep(2)
        pass
    except:
        print "Something that you need to fix"
    return render(request, 'dashboard/stop.html', {'server': server})
