from django.db import models
from datetime import datetime
from ASM.appium import manager
import os
from validators import validate_path, clean_executable_path
from django.core.exceptions import ValidationError
from ASM.settings import PROJECT_ROOT


class Appium_Executable(models.Model):
    display_name = models.CharField(max_length=500, default="Default Executable")
    installed_by_npm = models.BooleanField(default=True)
    executable_path = models.CharField(max_length=500, default="appium")
    node_path = models.CharField(max_length=500, blank=True, null=True)
    creation_date = models.DateTimeField('date created', default=datetime.now)

    def __str__(self):
        return self.display_name

    class Meta:
        verbose_name = 'Appium Configuration'
        verbose_name_plural = 'Appium Configurations'

    def executable_exists(self):
        return os.path.isfile(self.executable_path)

    def is_node_installed(self):
        return len(os.popen(self.node_path + " -v").read()) > 0

    def clean(self):
        if self.installed_by_npm is False:
            if os.path.isfile(self.executable_path) is False:
                raise ValidationError('Appium is not present in the path: %s' % self.executable_path)
            if os.path.isfile(self.node_path) is False and self.is_node_installed() is False:
                raise ValidationError('Node is not present in the specified path, is not installed, '
                                      'or is not specified in the environment variables : %s' % self.node_path)
        else:
            if self.executable_path not in os.popen('npm view "' + self.executable_path + '" name').read():
                raise ValidationError(self.executable_path + 'is not present as an NPM module')


class iOS_WebKit_Debug_Proxy(models.Model):
    display_name = models.CharField(max_length=50, default="iOS WebKit Debug Proxy Name")
    installed_by_npm = models.BooleanField(default=True)
    executable_path = models.CharField(max_length=500, default="appium")
    node_path = models.CharField(max_length=500, blank=True, null=True)
    creation_date = models.DateTimeField('date created', default=datetime.now)

    class Meta:
        verbose_name = 'iOS WebKit Debug Proxy Configuration'
        verbose_name_plural = 'iOS WebKit Debug Proxy Configurations'

    def executable_exists(self):
        return os.path.isfile(self.executable_path)

    def is_node_installed(self):
        return len(os.popen(self.node_path + " -v").read()) > 0

    def clean(self):
        if self.installed_by_npm is False:
            if os.path.isfile(self.executable_path) is False:
                raise ValidationError('iOS WebKit Debug Proxy is not present in the path: %s' % self.executable_path)
            if os.path.isfile(self.node_path) is False and self.is_node_installed() is False:
                raise ValidationError('Node is not present in the specified path, is not installed, '
                                      'or is not specified in the environment variables : %s' % self.node_path)
        else:
            if self.executable_path not in os.popen('npm view "' + self.executable_path + '" name').read():
                raise ValidationError(self.executable_path + 'is not present as an NPM module')


class Server(models.Model):
    server_name = models.CharField(max_length=50, default="Server Name")
    appium_executable = models.ForeignKey(Appium_Executable)
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
    udid = models.CharField(max_length=150, blank=True, null=True)
    is_iOS = models.BooleanField(default=False)
    is_iOS_Simulator = models.BooleanField(default=False)
    appium_executable = models.ForeignKey(iOS_WebKit_Debug_Proxy, blank=True, null=True)

    def __str__(self):
        return self.server_name

    def clean(self):
        if self.is_iOS is False and self.appium_executable is not None:
            raise ValidationError("iOS WebKit Debug Proxy is only allowed for iOS Devices")
        if self.is_iOS and self.is_iOS_Simulator is None and self.appium_executable is None:
            raise ValidationError("iOS WebKit Debug Proxy is required for real iOS Devices")

    def isActive(self):
        try:
            return manager.check_server_status(self.ip_address, self.port_number)
        except Exception as e:
            return False
    isActive.admin_order_field = 'server_status'
    isActive.boolean = True
    isActive.short_description = "Server Status"

    def read_log(self, server_id):
        log = open(os.path.join(PROJECT_ROOT+"/logs/", server_id + ".txt"))
        return log.read()

    def chromedriver_open(self):
        return manager.is_chromedriver_running(self.chromedriver_port)






