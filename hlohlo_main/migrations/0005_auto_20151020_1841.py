# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0004_auto_20151020_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subcategory',
            field=models.ForeignKey(to='hlohlo_main.Category', blank=True),
        ),
    ]
