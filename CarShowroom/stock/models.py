from django.db import models
from models.models import *


class Body_type(models.Model):
    id_body_type = models.AutoField('ID', primary_key=True, serialize=False)
    name = models.CharField('Тип кузова', max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'тип кузова'
        verbose_name_plural = '2. Типы кузова'


class Car_in_stock(models.Model):
    id_car_in_stock = models.AutoField('ID', primary_key=True, serialize=False)
    used = models.BooleanField('С пробегом')
    brand = models.CharField('Бренд', max_length=200)
    name = models.CharField('Модель', max_length=200)
    year = models.CharField('Год',max_length=50)
    engine_capacity = models.CharField('Объем двигателя', max_length=50)
    power = models.CharField('Мощность', max_length=50)
    id_fuel_type = models.ForeignKey(Fuel_type, verbose_name='Тип топлива', on_delete=models.CASCADE)
    id_transmission = models.ForeignKey(Transmission, verbose_name='Коробка передач', on_delete=models.CASCADE)
    id_drive_unit = models.ForeignKey(Drive_unit, verbose_name='Тип привода', on_delete=models.CASCADE)
    id_body_type = models.ForeignKey(Body_type, verbose_name='Тип кузова', on_delete=models.CASCADE)
    color = models.CharField('Цвет', max_length=200)
    mileage = models.CharField('Пробег', max_length=50)
    steering_wheel = models.BooleanField('Правый руль')
    generation = models.CharField('Поколение', max_length=200)
    car_equipment = models.CharField('Комплектация', max_length=200)
    description = models.TextField('Описание')
    card_picture = models.ImageField('Фото карточки', upload_to='car picture card')
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'автомобили на складе'
        verbose_name_plural = '1. Автомобили на складе'


class Car_picture(models.Model):
    id_car_picture = models.AutoField('ID', primary_key=True, serialize=False)
    id_car_in_stock = models.ForeignKey(Car_in_stock, verbose_name='Машина', on_delete=models.CASCADE)
    picture = models.ImageField('Фото', upload_to='car picture')

    def __str__(self):
        return self.id_car_in_stock.name

    class Meta:
        verbose_name = 'фото авто'
        verbose_name_plural = '2. Фото авто'