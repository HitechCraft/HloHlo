# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0008_auto_20151115_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='buyer',
            field=models.ForeignKey(related_name='buyer_profile', to=settings.AUTH_USER_MODEL, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='lot',
            name='count_viewers',
            field=models.IntegerField(verbose_name='Посетители', default=0),
        ),
        migrations.AlterUniqueTogether(
            name='lot',
            unique_together=set([]),
        ),
    ]
