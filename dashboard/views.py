from django.shortcuts import render, get_object_or_404
from ASM.appium.manager import start_appium_server

# Create your views here.
from django.http import HttpResponse
from .models import Server
from django.template import RequestContext, loader



def index(request):
    server_list = Server.objects.all()
    context = {'server_list': server_list}
    return render(request, 'dashboard/index.html', context)


def detail(request, server_id):
    server = get_object_or_404(Server, pk=server_id)
    return render(request, 'dashboard/detail.html', {'server': server})


def server_status(request, server_id):
    server = get_object_or_404(Server, pk=server_id)
    #if request.GET.get('startsrv'):
    start_appium_server(server.ip_address, server.port_number, server.chromedriver_port, server.bootstrap_port,
                        server.selendroid_port, "--no-reset --local-timezone")
    return render(request, 'dashboard/status.html', {'server': server})
