from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from ASM.appium.manager import start_appium_server, stop_appium_server
import time
import os

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from ASM.settings import PROJECT_ROOT
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


def log_viewer(request, server_id):
    log = open(os.path.join(PROJECT_ROOT+"/logs/", server_id + ".txt"))
    #response = HttpResponse(log.read())
    #response['Content-Disposition'] = 'inline;filename=some_file.txt'
    #return response
    #return render_to_response(({'log': log.read()}))


