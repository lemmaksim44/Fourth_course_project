from django.contrib.admin import AdminSite
from django.contrib.admin.forms import AdminAuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib import admin
from django.utils.safestring import mark_safe

from django.contrib.auth.models import Group, User
from company.models import *
from models.models import *
from services.models import *
from stock.models import *


class LimitedAdminSite(AdminSite):
    def login(self, request, extra_context=None):
        request.session.setdefault('login_attempts', 0)
        login_attempts = request.session.get('login_attempts', 0)
        if login_attempts >= 4:
            return HttpResponseRedirect('/pass_error')

        response = super().login(request, extra_context)

        if request.method == 'POST' and response.status_code == 302:
            del request.session['login_attempts']

        elif request.method == 'POST' and response.status_code == 200:
            request.session['login_attempts'] = login_attempts + 1

        return response

    def login_form(self, request, **kwargs):
        return AdminAuthenticationForm(request, **kwargs)

limited_admin_site = LimitedAdminSite(name='limited_admin')


class Request_Admin(admin.ModelAdmin):
    list_display = ('id_request', 'name_service', 'status')
    list_display_links = ('id_request', 'name_service', 'status')
    list_filter = ('name_service', 'status')


class Client_Admin(admin.ModelAdmin):
    list_display = ('id_client',)
    search_fields = ('client_name', 'client_phone', 'client_email',)


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


limited_admin_site.register(Request, Request_Admin)
limited_admin_site.register(Client, Client_Admin)

limited_admin_site.register(Brand, Brand_Admin)
limited_admin_site.register(Model, Model_Admin)
limited_admin_site.register(Model_picture, Model_picture_Admin)
limited_admin_site.register(Modification, Modification_Admin)
limited_admin_site.register(Car_equipment, Car_equipment_Admin)
limited_admin_site.register(Class, Class_Admin)
limited_admin_site.register(Fuel_type, Fuel_type_Admin)
limited_admin_site.register(Transmission, Transmission_Admin)
limited_admin_site.register(Drive_unit, Drive_unit_Admin)

limited_admin_site.register(Operating_tips, Operating_tips_Admin)
limited_admin_site.register(Region, Region_Admin)
limited_admin_site.register(City, City_Admin)

limited_admin_site.register(Body_type, Body_type_Admin)
limited_admin_site.register(Car_in_stock, Car_in_stock_Admin)

limited_admin_site.register(User)
limited_admin_site.register(Group)

limited_admin_site.site_header = 'Атик-Моторс'




"""
from django.contrib import admin


admin.site.site_header = 'Атик-Моторс'

"""
