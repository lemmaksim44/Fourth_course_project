# Generated by Django 4.1.7 on 2023-05-11 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_in_stock',
            name='engine_capacity',
            field=models.CharField(max_length=50, verbose_name='Объем двигателя'),
        ),
    ]