# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extuser', '0002_auto_20151020_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extuser',
            name='user_type',
            field=models.IntegerField(choices=[(0, 'Частное лицо'), (1, 'Компания')], default=0, verbose_name='Тип пользователя'),
        ),
    ]
