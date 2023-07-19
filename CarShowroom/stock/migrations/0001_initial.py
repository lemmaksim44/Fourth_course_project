# Generated by Django 4.1.7 on 2023-04-15 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('models', '0005_alter_modification_engine_power'),
    ]

    operations = [
        migrations.CreateModel(
            name='Body_type',
            fields=[
                ('id_body_type', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Тип кузова')),
            ],
            options={
                'verbose_name': 'тип кузова',
                'verbose_name_plural': '3. Типы кузова',
            },
        ),
        migrations.CreateModel(
            name='Car_in_stock',
            fields=[
                ('id_car_in_stock', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('used', models.BooleanField(verbose_name='С пробегом')),
                ('brand', models.CharField(max_length=200, verbose_name='Бренд')),
                ('name', models.CharField(max_length=200, verbose_name='Модель')),
                ('year', models.CharField(max_length=50, verbose_name='Год')),
                ('engine_capacity', models.CharField(max_length=50, verbose_name='Мощность двигателя')),
                ('power', models.CharField(max_length=50, verbose_name='Мощность')),
                ('color', models.CharField(max_length=200, verbose_name='Цвет')),
                ('mileage', models.CharField(max_length=50, verbose_name='Пробег')),
                ('steering_wheel', models.BooleanField(verbose_name='Правый руль')),
                ('generation', models.CharField(max_length=200, verbose_name='Поколение')),
                ('car_equipment', models.CharField(max_length=200, verbose_name='Комплектация')),
                ('description', models.TextField(verbose_name='Описание')),
                ('card_picture', models.ImageField(upload_to='car picture card', verbose_name='Фото карточки')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('id_body_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.body_type', verbose_name='Тип кузова')),
                ('id_drive_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.drive_unit', verbose_name='Тип привода')),
                ('id_fuel_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.fuel_type', verbose_name='Тип топлива')),
                ('id_transmission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.transmission', verbose_name='Коробка передач')),
            ],
            options={
                'verbose_name': 'машину на складе',
                'verbose_name_plural': '1. Машины на складе',
            },
        ),
        migrations.CreateModel(
            name='Car_picture',
            fields=[
                ('id_car_picture', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='car picture', verbose_name='Фото')),
                ('id_car_in_stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.car_in_stock', verbose_name='Машина')),
            ],
            options={
                'verbose_name': 'фото авто',
                'verbose_name_plural': '2. Фото авто',
            },
        ),
    ]