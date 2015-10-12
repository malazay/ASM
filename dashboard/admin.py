from django.contrib import admin
from import_export import resources
from .models import Server, Appium_Executable
from import_export.admin import ImportExportModelAdmin, ImportExportMixin


class ServerResource(resources.ModelResource):

    class Meta:
        model = Server
        skip_unchanged = True
        report_skipped = True
        exclude = ('server_status', 'full_reset', 'no_reset', 'session_override', 'creation_date', 'command_timeout')


class AppiumAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Appium executable display name', {'fields': ['display_name']}),
        ('Is Appium installed by NPM?', {'fields': ['installed_by_npm']}),
        ('Appium Executable Path', {'fields': ['executable_path']}),
        ('Node Path', {'fields': ['node_path']}),
        ('Creation Date', {'fields': ['creation_date'], 'classes': ['collapse']}),
        ]
    list_display = ('display_name', 'installed_by_npm', 'executable_path', 'node_path')


class ServerAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = ServerResource
    fieldsets = [
        ('Appium Config',               {'fields': ['appium_executable']}),
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
dataset = ServerResource().export()
