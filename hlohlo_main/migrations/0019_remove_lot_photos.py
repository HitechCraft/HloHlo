# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0018_lot_photos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lot',
            name='photos',
        ),
    ]
