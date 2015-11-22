# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hlohlo_main', '0016_lot_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=''),
            preserve_default=False,
        ),
    ]
