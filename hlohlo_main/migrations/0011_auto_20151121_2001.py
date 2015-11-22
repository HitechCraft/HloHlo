# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hlohlo_main', '0010_auto_20151115_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='LotRater',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('rate', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='lot',
            name='active',
            field=models.BooleanField(default=1),
        ),
        migrations.AddField(
            model_name='lot',
            name='price_buy_now',
            field=models.FloatField(verbose_name='Цена купить сейчас', default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lot',
            name='price',
            field=models.FloatField(verbose_name='Актуальная цена'),
        ),
        migrations.AddField(
            model_name='lotrater',
            name='lot',
            field=models.OneToOneField(to='hlohlo_main.Lot'),
        ),
        migrations.AddField(
            model_name='lotrater',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
