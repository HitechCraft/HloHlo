# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0002_auto_20151115_1900'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lot',
            unique_together=set([('author',)]),
        ),
    ]
