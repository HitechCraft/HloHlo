# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0011_auto_20151115_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
