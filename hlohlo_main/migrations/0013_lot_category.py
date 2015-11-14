# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0012_auto_20151115_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='category',
            field=models.ManyToManyField(to='hlohlo_main.Category'),
        ),
    ]
