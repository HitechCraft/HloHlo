from django.db import models
from extuser.models import ExtUser

class Lot(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    type_auction = models.BooleanField('Купить сейчас', default=False)
    time_create = models.DateTimeField('Дата создания')
    time_life = models.IntegerField('Прошло времени')
    price = models.FloatField('Цена')
    photos = []
    category = []
    count_viewers = models.IntegerField('Посетители')
    author = models.OneToOneField(ExtUser, related_name='author_profile')
    buyer = models.OneToOneField(ExtUser, related_name='buyer_profile')
    # Subscribers = ForeignKey(ExtUser, related_name='subscriber_profiles')

    def __str__(self):

        return self.name

    class Meta:
        verbose_name = 'лот'
        verbose_name_plural = 'лоты'


class Category(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', max_length=1500)
    sub_category = models.OneToOneField('self')

    def __str__(self):

        return self.name

class Lots(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    lots = models.ForeignKey('Lot')

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
    cityDistricts = models.ForeignKey('CityDistrict')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'

class Region(models.Model):
    name = models.CharField('Название', max_length=255)
    cities = models.ForeignKey('City')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'регион'
        verbose_name_plural = 'регионы'