from django.db import models
from datetime import datetime

class Server(models.Model):
    server_name = models.CharField(max_length=50, default="Server Name")
    ip_address = models.CharField(max_length=20, default="127.0.0.1")
    port_number = models.CharField(max_length=5)
    chromedriver_port = models.CharField(max_length=5)
    bootstrap_port = models.CharField(max_length=5)
    selendroid_port = models.CharField(max_length=5)
    creation_date = models.DateTimeField('date created', default=datetime.now)
    server_status = models.BooleanField(default=False)

    def __str__(self):
        return self.server_name

    def isActive(self):
        return self.server_status
    isActive.admin_order_field = 'server_status'
    isActive.boolean = True
    isActive.short_description = "Server Status"
