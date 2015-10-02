from django.db import models
from datetime import datetime
from ASM.appium import manager
import os
from ASM.settings import PROJECT_ROOT


class Server(models.Model):
    server_name = models.CharField(max_length=50, default="Server Name")
    ip_address = models.CharField(max_length=20, default="127.0.0.1")
    port_number = models.CharField(max_length=5)
    chromedriver_port = models.CharField(max_length=5)
    bootstrap_port = models.CharField(max_length=5)
    selendroid_port = models.CharField(max_length=5)
    creation_date = models.DateTimeField('date created', default=datetime.now)
    command_timeout = models.IntegerField(default=120)
    server_status = models.BooleanField(default=False)
    full_reset = models.BooleanField(default=True)
    no_reset = models.BooleanField(default=False)
    session_override = models.BooleanField(default=True)

    def __str__(self):
        return self.server_name

    def isActive(self):
        return manager.check_server_status(self.ip_address, self.port_number)
    isActive.admin_order_field = 'server_status'
    isActive.boolean = True
    isActive.short_description = "Server Status"

    def read_log(self, server_id):
        log = open(os.path.join(PROJECT_ROOT+"/logs/", server_id + ".txt"))
        return log.read()
