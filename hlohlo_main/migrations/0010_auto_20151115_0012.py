# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0009_auto_20151115_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='sub_category',
            field=models.ManyToManyField(to='hlohlo_main.Category', blank=True, null=True, related_name='_sub_category_+'),
        ),
    ]
