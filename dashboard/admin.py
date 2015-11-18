from django.contrib import admin
from import_export import resources
from .models import Server, Appium_Executable, iOS_WebKit_Debug_Proxy
from import_export.admin import ImportExportModelAdmin, ImportExportMixin


class ServerResource(resources.ModelResource):
    class Meta:
        model = Server
        skip_unchanged = True
        report_skipped = True
        exclude = ('server_status', 'full_reset', 'no_reset', 'session_override', 'creation_date', 'command_timeout',
                   'is_iOS', 'is_iOS_Simulator', 'appium_executable')


class AppiumAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Appium executable display name', {'fields': ['display_name']}),
        ('Is Appium installed by NPM?', {'fields': ['installed_by_npm']}),
        ('Appium Executable Path', {'fields': ['executable_path']}),
        ('Node Path', {'fields': ['node_path']}),
        ('Creation Date', {'fields': ['creation_date'], 'classes': ['collapse']}),
        ]
    list_display = ('display_name', 'installed_by_npm', 'executable_path', 'node_path')


class WebKitProxyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('iOS WebKit Debug Proxy Name', {'fields': ['display_name']}),
        ('Port', {'fields': ['port']}),
        ('Installed by Brew?', {'fields': ['installed_by_brew']}),
        ('iOS WebKit Proxy Executable Path', {'fields': ['executable_path']}),
        ('Node Path', {'fields': ['node_path']}),
        ('Creation Date', {'fields': ['creation_date'], 'classes': ['collapse']}),
        ]
    list_display = ('display_name', 'port', 'installed_by_brew', 'executable_path', 'node_path')


class ServerAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = ServerResource
    fieldsets = [
        ('Appium Config', {'fields': ['appium_executable']}),
        ('iOS Server', {'fields': ['is_iOS']}),
        ('iOS Simulator', {'fields': ['is_iOS_Simulator']}),
        ('iOS WebKit Debug Proxy Config', {'fields': ['webkit_executable']}),
        ('Server Name', {'fields': ['server_name']}),
        ('IP Address', {'fields': ['ip_address']}),
        ('Port Number', {'fields': ['port_number']}),
        ('Chromedriver Port', {'fields': ['chromedriver_port']}),
        ('Bootstrap Port', {'fields': ['bootstrap_port']}),
        ('Selendroid Port', {'fields': ['selendroid_port']}),
        ('Command Timeout', {'fields': ['command_timeout']}),
        ('Full Reset', {'fields': ['full_reset']}),
        ('No Reset', {'fields': ['no_reset']}),
        ('Session Override', {'fields': ['session_override']}),
        ('Creation Date', {'fields': ['creation_date'], 'classes': ['collapse']}),
        ('UDID', {'fields': ['udid']}),
        ]
    list_display = ('server_name', 'ip_address', 'port_number', 'chromedriver_port', 'bootstrap_port',
                    'selendroid_port', 'creation_date', 'isActive')
    list_filter = ['server_name', 'ip_address', 'port_number', 'server_status']
    search_fields = ['server_name', 'ip_address', 'port_number', 'server_status']


class ServerAdminExportImport(ImportExportModelAdmin):
    resource_class = ServerResource
    pass

admin.site.register(Server, ServerAdmin)
admin.site.register(Appium_Executable, AppiumAdmin)
admin.site.register(iOS_WebKit_Debug_Proxy, WebKitProxyAdmin)
#dataset = ServerResource().export()
