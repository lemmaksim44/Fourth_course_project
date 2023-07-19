""""
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class Operating_tips_Admin(admin.ModelAdmin):
    list_display = ('id_operating_tips', 'card_picture', 'title')
    list_display_links = ('id_operating_tips', 'card_picture', 'title')
    search_fields = ('title',)
    fields = ('card_picture', 'picture', 'title', 'text')
    readonly_fields = ('card_picture',)

    def card_picture(self, object):
        return mark_safe(f"<img src='{object.picture.url}' width = 200 height = 120>")

    card_picture.short_description = 'Фото'


class Region_Admin(admin.ModelAdmin):
    list_display = ('id_region', 'name')
    list_display_links = ('id_region', 'name')
    search_fields = ('name',)


class City_Admin(admin.ModelAdmin):
    list_display = ('id_city', 'id_region', 'name', 'coefficient')
    list_display_links = ('id_city', 'id_region', 'name', 'coefficient')
    search_fields = ('name',)


admin.site.register(Operating_tips, Operating_tips_Admin)
admin.site.register(Region, Region_Admin)
admin.site.register(City, City_Admin)
"""