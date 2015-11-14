# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0015_auto_20151115_0143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lot',
            name='album',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='album',
        ),
        migrations.AddField(
            model_name='photo',
            name='lot',
            field=models.ForeignKey(to='hlohlo_main.Lot', default=''),
        ),
        migrations.DeleteModel(
            name='Album',
        ),
    ]
