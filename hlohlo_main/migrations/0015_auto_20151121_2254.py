# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0014_auto_20151121_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='price_buy_now',
            field=models.FloatField(default=0, verbose_name='Цена купить сейчас', blank=True, null=True),
        ),
    ]
