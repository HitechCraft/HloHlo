# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0003_auto_20151106_2022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lots',
            options={'verbose_name': 'коллекция лотов', 'verbose_name_plural': 'коллекции лотов'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'регион', 'verbose_name_plural': 'регионы'},
        ),
    ]
