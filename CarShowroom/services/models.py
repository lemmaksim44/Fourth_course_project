from django.db import models


class Operating_tips(models.Model):
    id_operating_tips = models.AutoField('ID', primary_key=True, serialize=False)
    picture = models.ImageField('Фото карточки', upload_to='operating tips')
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Текст')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'статью'
        verbose_name_plural = '1. Советы по эксплуатации'


class Region(models.Model):
    id_region = models.AutoField('ID', primary_key=True, serialize=False)
    name = models.CharField('Область/Регион', max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'регион'
        verbose_name_plural = '2. Области и регионы'


class City(models.Model):
    id_city = models.AutoField('ID', primary_key=True, serialize=False)
    id_region = models.ForeignKey(Region, verbose_name='Область/Регион', on_delete=models.CASCADE)
    name = models.CharField('Название города', max_length=200)
    coefficient = models.FloatField('Коэффициент города')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'город'
        verbose_name_plural = '3. Города'