from django.db import models
from extuser.models import ExtUser


class Category(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', max_length=1500, blank=True)
    sub_category = models.ManyToManyField('self', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категории лотов'
        verbose_name_plural = 'категории лотов'


class Lot(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    type_auction = models.BooleanField('Купить сейчас', default=False)
    time_create = models.DateTimeField('Дата создания')
    time_life = models.IntegerField('Прошло времени')
    price = models.FloatField('Цена')
    category = models.ManyToManyField(Category)
    count_viewers = models.IntegerField('Посетители')
    author = models.ForeignKey(ExtUser, related_name='author_profile')
    buyer = models.ForeignKey(ExtUser, related_name='buyer_profile')
    # Subscribers = ForeignKey(ExtUser, related_name='subscriber_profiles')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'лот'
        verbose_name_plural = 'лоты'


class Photo(models.Model):
    lot = models.ForeignKey(Lot, default='', verbose_name='Лот')
    file = models.ImageField("Фото", upload_to='images', help_text='Желательно, чтоб фото было не большого размера')
    
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Collection(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    lots = models.ManyToManyField(Lot, verbose_name='Лот')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'коллекция лотов'
        verbose_name_plural = 'коллекции лотов'


class CityDistrict(models.Model):
    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'район'
        verbose_name_plural = 'районы'


class City(models.Model):
    name = models.CharField('Название', max_length=255)
    cityDistricts = models.ManyToManyField('CityDistrict')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'


class Region(models.Model):
    name = models.CharField('Название', max_length=255)
    cities = models.ManyToManyField('City')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'регион'
        verbose_name_plural = 'регионы'
