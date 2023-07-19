from django.db import models


class Fuel_type(models.Model):
    id_fuel_type = models.AutoField('ID', primary_key=True, serialize=False)
    name = models.CharField('Тип топлива', max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'тип топлива'
        verbose_name_plural = '7. Типы топлива'


class Transmission(models.Model):
    id_transmission = models.AutoField('ID', primary_key=True, serialize=False)
    name = models.CharField('Тип трансмиссии', max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'тип трансмиссии'
        verbose_name_plural = '8. Типы трансмиссий'


class Drive_unit(models.Model):
    id_drive_unit = models.AutoField('ID', primary_key=True, serialize=False)
    name = models.CharField('Тип привода', max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'тип привода'
        verbose_name_plural = '9. Типы привода'


class Brand(models.Model):
    id_brand = models.AutoField('ID', primary_key=True, serialize=False)
    logo = models.ImageField('Логотип', upload_to='logo')
    name = models.CharField('Бренд', max_length=50)
    address = models.CharField('Адрес автосалона', max_length=100)
    phone = models.CharField('Телефон автосалона', max_length=20)
    main_picture = models.ImageField('Фото на главной странице моделей', upload_to='main models')
    link = models.CharField('Ссылка на сайт партнера', max_length=250)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'бренд'
        verbose_name_plural = '1. Бренды'
    

class Class(models.Model):
    id_class = models.AutoField('ID', primary_key=True, serialize=False)
    name = models.CharField('Название класса', max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'класс авто'
        verbose_name_plural = '6. Классы авто'


class Model(models.Model):
    id_model = models.AutoField('ID', primary_key=True, serialize=False)
    id_brand = models.ForeignKey(Brand, verbose_name='Бренд', on_delete=models.CASCADE)
    id_class = models.ForeignKey(Class, verbose_name='Класс авто', on_delete=models.CASCADE)
    name = models.CharField('Название модели', max_length=100)
    card_pictures = models.ImageField('Фото для карточки', upload_to='model')
    description = models.TextField('Описание авто')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'модель'
        verbose_name_plural = '2. Модели'


class Model_picture(models.Model):
    id_model_picture = models.AutoField('ID', primary_key=True, serialize=False)
    id_model = models.ForeignKey(Model, verbose_name='Модель', on_delete=models.CASCADE)
    picture_1 = models.ImageField('Главное изображение', upload_to='model picture')
    picture_2 = models.ImageField('Второстепенное изображение', upload_to='model picture')
    picture_3 = models.ImageField('Второстепенное изображение', upload_to='model picture')

    def __str__(self):
        return self.id_model.name
    
    class Meta:
        verbose_name = 'изображение модели'
        verbose_name_plural = '3. Изображения моделей'


class Modification(models.Model):
    id_modification = models.AutoField('ID', primary_key=True, serialize=False)
    id_model = models.ForeignKey(Model, verbose_name='Модель', on_delete=models.CASCADE)
    engine_capacity = models.FloatField('Объем двигателя', max_length=5)
    engine_power = models.IntegerField('Мощность двигателя')
    id_fuel_type = models.ForeignKey(Fuel_type, verbose_name='Тип топлива', on_delete=models.CASCADE)
    id_transmission = models.ForeignKey(Transmission, verbose_name='Тип трансмиссии', on_delete=models.CASCADE)
    id_drive_unit = models.ForeignKey(Drive_unit, verbose_name='Тип привода', on_delete=models.CASCADE)

    def __str__(self):
        return self.id_model.name
    
    class Meta:
        verbose_name = 'модификацию'
        verbose_name_plural = '4. Модификации'


class Car_equipment(models.Model):
    id_car_equipment = models.AutoField('ID', primary_key=True, serialize=False)
    id_model = models.ForeignKey(Model, verbose_name='Модель', on_delete=models.CASCADE)
    name = models.CharField('Название комплектации', max_length=100)
    description = models.TextField('Описание комплектации')
    price = models.IntegerField('Цена комплектации')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'комплектацию'
        verbose_name_plural = '5. Комплектации'

