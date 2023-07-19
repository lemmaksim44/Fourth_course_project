"""
from django.contrib import admin
from .models import *


class Request_Admin(admin.ModelAdmin):
    list_display = ('id_request', 'name_service', 'status')
    list_display_links = ('id_request', 'name_service', 'status')
    list_filter = ('name_service', 'status')


class Client_Admin(admin.ModelAdmin):
    list_display = ('id_client',)
    search_fields = ('client_name', 'client_phone', 'client_email',)


admin.site.register(Request, Request_Admin)
admin.site.register(Client, Client_Admin)
"""

