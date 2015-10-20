# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lot',
            old_name='Author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='lot',
            old_name='Buyer',
            new_name='buyer',
        ),
    ]
