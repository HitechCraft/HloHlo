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
