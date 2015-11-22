# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0012_auto_20151121_2022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lotrater',
            old_name='user',
            new_name='rater',
        ),
    ]
