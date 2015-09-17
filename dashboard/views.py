from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Server
from django.template import RequestContext, loader


def index(request):
    server_list = Server.objects.all()
    context = {'server_list': server_list}
    return render(request, 'dashboard/index.html', context)


def server_details(request):
    return request("Here is where all the server details will be displayed")
