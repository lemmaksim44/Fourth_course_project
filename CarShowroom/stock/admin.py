""""
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class Body_type_Admin(admin.ModelAdmin):
    list_display = ('id_body_type', 'name')
    list_display_links = ('id_body_type', 'name')
    search_fields = ('name',)


class Car_in_stock_Admin(admin.ModelAdmin):
    list_display = ('id_car_in_stock', 'picture', 'used', 'brand', 'name', 'year', 'price')
    list_display_links = ('id_car_in_stock', 'picture', 'brand', 'name', 'year', 'price')
    readonly_fields = ('picture',)
    fields = ('used', 'brand', 'name', 'year', 'engine_capacity', 'power',
              'id_fuel_type', 'id_transmission', 'id_drive_unit', 'id_body_type',
              'color', 'mileage', 'steering_wheel', 'generation', 'car_equipment',
              'description', 'picture', 'card_picture', 'price')
    list_filter = ('used', 'brand', 'year')
    search_fields = ('brand', 'name')

    def picture(self, object):
        return mark_safe(f"<img src='{object.card_picture.url}' width = 200 height = 120>")
    
    picture.short_description = 'Фото'


admin.site.register(Body_type, Body_type_Admin)
admin.site.register(Car_in_stock, Car_in_stock_Admin)
"""