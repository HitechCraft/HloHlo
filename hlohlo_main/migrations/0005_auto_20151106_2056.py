# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0004_auto_20151106_2041'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'город', 'verbose_name_plural': 'города'},
        ),
        migrations.AlterModelOptions(
            name='citydistrict',
            options={'verbose_name': 'район', 'verbose_name_plural': 'районы'},
        ),
    ]
