# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0013_lot_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lots',
            new_name='Collection',
        ),
    ]
