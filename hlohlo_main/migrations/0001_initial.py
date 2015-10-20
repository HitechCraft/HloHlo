# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Название', max_length=255)),
                ('description', models.TextField(verbose_name='Описание')),
                ('type_auction', models.BooleanField(verbose_name='Купить сейчас', default=False)),
                ('time_create', models.DateTimeField(verbose_name='Дата создания')),
                ('time_life', models.IntegerField(verbose_name='Прошло времени')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('count_viewers', models.IntegerField(verbose_name='Посетители')),
                ('Author', models.OneToOneField(related_name='author_profile', to=settings.AUTH_USER_MODEL)),
                ('Buyer', models.OneToOneField(related_name='buyer_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
