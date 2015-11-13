# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0006_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='cityDistricts',
        ),
        migrations.AddField(
            model_name='city',
            name='cityDistricts',
            field=models.ManyToManyField(to='hlohlo_main.CityDistrict'),
        ),
        migrations.RemoveField(
            model_name='lots',
            name='lots',
        ),
        migrations.AddField(
            model_name='lots',
            name='lots',
            field=models.ManyToManyField(to='hlohlo_main.Lot'),
        ),
        migrations.RemoveField(
            model_name='region',
            name='cities',
        ),
        migrations.AddField(
            model_name='region',
            name='cities',
            field=models.ManyToManyField(to='hlohlo_main.City'),
        ),
    ]
