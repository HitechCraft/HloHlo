from django.db import models
from datetime import datetime, time, timedelta, timezone
from django.utils.dateformat import DateFormat
from extuser.models import ExtUser
from django.contrib import admin

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
    time_create = models.DateTimeField('Дата создания', auto_now_add=True)
    time_life = models.IntegerField('Время на аукцион (в днях)')
    price = models.FloatField('Цена')
    category = models.ManyToManyField(Category)
    count_viewers = models.IntegerField('Посетители', default=0)
    author = models.ForeignKey(ExtUser, related_name='author_profile', default='', null=True)
    buyer = models.ForeignKey(ExtUser, related_name='buyer_profile', default='', null=True)
    # Subscribers = ForeignKey(ExtUser, related_name='subscriber_profiles')

    def getTimeLeft(self): #костыль By Random
        time_string = ''
        current_time = datetime.now(timezone.utc)
        time_differ = self.time_create + timedelta(days=self.time_life) - current_time
        to_sec = time_differ.total_seconds()

        days = str(time_differ.days)
        hours = str(int(to_sec // 3600))
        mins = str(int((to_sec % 3600) // 60))
        secs = str(int(to_sec % 60))

        if days != 0: time_string += days + " дн. "
        if hours != 0: time_string += hours + " ч. "
        if mins != 0: time_string += mins + " м. "
        if secs != 0: time_string += secs + " с. "

        return time_string

    def __str__(self):
        return self.name

    class Meta:
        #unique_together = ('author',)
        verbose_name = 'лот'
        verbose_name_plural = 'лоты'


class Photo(models.Model):
    lot = models.ForeignKey(Lot, default='', verbose_name='Лот')
    file = models.ImageField("Фото", upload_to='images', help_text='Форматы: png, jpg, jpeg, bmp. gif')

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
