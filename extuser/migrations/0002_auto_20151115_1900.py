# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extuser',
            name='user_type',
            field=models.IntegerField(default=0, choices=[(0, 'Частное лицо'), (1, 'Компания')], verbose_name='Тип пользователя'),
        ),
    ]
