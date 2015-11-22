# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0015_auto_20151121_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
