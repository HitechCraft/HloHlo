from django.db import models
from datetime import datetime, time, timedelta, timezone
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
    time_create = models.DateTimeField('Дата создания', auto_now_add=True)
    time_life = models.IntegerField('Время на аукцион (в днях)')
    price = models.FloatField('Цена')
    category = models.ManyToManyField(Category)
    count_viewers = models.IntegerField('Посетители', default=0)
    author = models.ForeignKey(ExtUser, related_name='author_profile', default='', null=True)
    buyer = models.ForeignKey(ExtUser, related_name='buyer_profile', default='', null=True)
    # Subscribers = ForeignKey(ExtUser, related_name='subscriber_profiles')

    def getTimeLeft(self):
        time_string = ''
        current_time = datetime.now(timezone.utc)
        time_differ = self.time_create + timedelta(days=self.time_life) - current_time
        temp=str(time_differ)
        return temp
        temp1=temp.split(' ')[2]
        days=int(temp.split(' ')[0])
        hours=int(temp1.split(':')[0])
        mins=int(temp1.split(':')[1])
        secs=int(temp1.split(':')[2].split('.')[0])

        if days >= 1 and hours >= 0:
            time_string = "{0} дн. {1} ч.".format(days, hours)
            return time_string
        elif hours >= 1 and mins >= 0:
            time_string = "{0} ч. {1} м.".format(hours, mins)
            return time_string
        elif mins >= 1 and secs >= 0:
            time_string = "{0} м. {1} с.".format(mins, secs)
            return time_string
        elif secs >= 1:
            time_string = "{0} с.".format(secs)
            return time_string

    def __str__(self):
        return self.name

    class Meta:
        # unique_together = ('author',)
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
