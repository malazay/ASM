from django.contrib import admin
from .models import Server


class ServerAdmin(admin.ModelAdmin):
    fieldsets = [
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
        ('Creation Date', {'fields': ['creation_date'], 'classes': ['collapse']})
        ]


    list_display = ('server_name', 'ip_address', 'port_number', 'chromedriver_port', 'bootstrap_port',
                    'selendroid_port', 'creation_date', 'isActive')
    list_filter = ['server_name', 'ip_address', 'port_number', 'server_status']
    search_fields = ['server_name', 'ip_address', 'port_number', 'server_status']


admin.site.register(Server, ServerAdmin)
