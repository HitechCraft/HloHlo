from django.db import models

class Lot(models.Model):

    name = models.CharField('Название',max_length=255)
    description = models.TextField('Описание')
    type_auction = models.BooleanField('Купить сейчас')
    time_create = models.DateTimeField('Дата создания')
    time_life = models.IntegerField('Прошло времени')
    price = models.FloatField('Цена')
    photos = []
    category = []
    count_viewers = models.IntegerField('Посетители')
    Author = models.ForeignKey(extuser)
    Buyer = models.ForeignKey(extuser)
    #Subscribers
    #
# Create your models here.

