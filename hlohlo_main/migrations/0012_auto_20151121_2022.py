# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0011_auto_20151121_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lotrater',
            name='lot',
            field=models.ForeignKey(verbose_name='Лот', default='', to='hlohlo_main.Lot'),
        ),
    ]
