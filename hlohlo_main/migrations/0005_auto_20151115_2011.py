# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0004_auto_20151115_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='author',
            field=models.ForeignKey(related_name='author_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
