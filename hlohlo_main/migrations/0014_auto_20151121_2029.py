# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0013_auto_20151121_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lotrater',
            name='rater',
            field=models.ForeignKey(verbose_name='Покупатель', default='', to=settings.AUTH_USER_MODEL),
        ),
    ]
