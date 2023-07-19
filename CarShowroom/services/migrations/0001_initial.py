# Generated by Django 4.1.7 on 2023-04-11 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operating_tips',
            fields=[
                ('id_operating_tips', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='operating tips', verbose_name='Фото карточки')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'статью',
                'verbose_name_plural': 'Советы по эксплуатации',
            },
        ),
    ]
