""""
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class Brand_Admin(admin.ModelAdmin):
    list_display = ('id_brand', 'logo_picture', 'name')
    list_display_links = ('id_brand', 'logo_picture', 'name')
    fields = ('logo_picture', 'logo', 'name', 'address', 'phone', 'picture', 'main_picture', 'link')
    readonly_fields = ('logo_picture','picture',)

    def logo_picture(self, object):
        return mark_safe(f"<img src='{object.logo.url}' width = 100 height = 50>")
    
    def picture(self, object):
        return mark_safe(f"<img src='{object.main_picture.url}' width = 300 height = 150>")
    
    logo_picture.short_discriptions = 'Фото логотипа'
    picture.short_discriptions = 'Фото на странице бренда'


class Model_Admin(admin.ModelAdmin):
    list_display = ('id_model', 'picture', 'id_brand', 'name')
    list_display_links = ('id_model', 'picture', 'id_brand', 'name')
    list_filter = ('id_brand',)
    fields = ('id_brand', 'id_class', 'name', 'picture', 'card_pictures', 'description')
    readonly_fields = ('picture',)
    search_fields = ('name',)

    def picture(self, object):
        return mark_safe(f"<img src='{object.card_pictures.url}' width = 150 height = 70>")
    
    picture.short_description = 'Фото авто'


class Model_picture_Admin(admin.ModelAdmin):
    list_display = ('id_model_picture', 'id_model', 'picture1', 'picture2', 'picture3')
    list_display_links = ('id_model_picture', 'id_model', 'picture1', 'picture2', 'picture3')
    fields = ('id_model', 'picture1', 'picture_1', 'picture2', 'picture_2', 'picture3', 'picture_3')
    readonly_fields = ('picture1', 'picture2', 'picture3')
    search_fields = ('id_model__name',)

    def picture1(self, object):
        return mark_safe(f"<img src='{object.picture_1.url}' width = 150 height = 70>")
    
    def picture2(self, object):
        return mark_safe(f"<img src='{object.picture_2.url}' width = 150 height = 70>")
    
    def picture3(self, object):
        return mark_safe(f"<img src='{object.picture_3.url}' width = 150 height = 70>")

    picture1.short_description = 'Фото авто'
    picture2.short_description = 'Фото авто'
    picture3.short_description = 'Фото авто'


class Modification_Admin(admin.ModelAdmin):
    list_display = ('id_modification', 'id_model')
    list_display_links = ('id_modification', 'id_model')
    search_fields = ('id_model__name',)


class Car_equipment_Admin(admin.ModelAdmin):
    list_display = ('id_car_equipment', 'id_model', 'name', 'price')
    list_display_links = ('id_car_equipment', 'id_model', 'name', 'price')
    search_fields = ('id_model__name', 'name')


class Class_Admin(admin.ModelAdmin):
    list_display = ('id_class', 'name')
    list_display_links = ('id_class', 'name')
    search_fields = ('name',)


class Fuel_type_Admin(admin.ModelAdmin):
    list_display = ('id_fuel_type', 'name')
    list_display_links = ('id_fuel_type', 'name')
    search_fields = ('name',)


class Transmission_Admin(admin.ModelAdmin):
    list_display = ('id_transmission', 'name')
    list_display_links = ('id_transmission', 'name')
    search_fields = ('name',)


class Drive_unit_Admin(admin.ModelAdmin):
    list_display = ('id_drive_unit', 'name')
    list_display_links = ('id_drive_unit', 'name')
    search_fields = ('name',)


admin.site.register(Brand, Brand_Admin)
admin.site.register(Model, Model_Admin)
admin.site.register(Model_picture, Model_picture_Admin)
admin.site.register(Modification, Modification_Admin)
admin.site.register(Car_equipment, Car_equipment_Admin)
admin.site.register(Class, Class_Admin)
admin.site.register(Fuel_type, Fuel_type_Admin)
admin.site.register(Transmission, Transmission_Admin)
admin.site.register(Drive_unit, Drive_unit_Admin)
"""