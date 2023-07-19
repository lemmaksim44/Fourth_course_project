from django.db import models


class Request(models.Model):
    id_request = models.AutoField('ID', primary_key=True, serialize=False)
    name_service = models.CharField('Услуга', max_length=200)
    client_name = models.CharField('Имя клиента', max_length=200)
    client_phone = models.CharField('Телефон', max_length=11)
    client_email = models.CharField('Email', max_length=200, null=True, blank=True)
    comment = models.TextField('Комментарий', null=True, blank=True)
    status = models.BooleanField('Статус обработки')

    def __str__(self):
        return self.name_service
    
    class Meta:
        verbose_name = 'запрос'
        verbose_name_plural = '1. Запросы'


class Client(models.Model):
    id_client = models.AutoField('ID', primary_key=True, serialize=False)
    client_name = models.CharField('Имя клиента', max_length=200)
    client_phone = models.CharField('Телефон', max_length=11)
    client_email = models.CharField('Email', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name = 'клиента'
        verbose_name_plural = '2. Клиенты'