# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0009_auto_20151115_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='author_profile', default=''),
        ),
    ]
