# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0003_auto_20151115_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='count_viewers',
            field=models.IntegerField(default=0, verbose_name='Посетители'),
        ),
    ]
