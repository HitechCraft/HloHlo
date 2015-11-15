# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0007_auto_20151115_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='buyer',
            field=models.ForeignKey(default='', related_name='buyer_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lot',
            name='count_viewers',
            field=models.IntegerField(verbose_name='Посетители'),
        ),
    ]
