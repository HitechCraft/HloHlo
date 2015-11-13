# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0005_auto_20151106_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(max_length=1500, verbose_name='Описание')),
                ('sub_category', models.OneToOneField(to='hlohlo_main.Category')),
            ],
            options={
                'verbose_name_plural': 'категории лотов',
                'verbose_name': 'категории лотов',
            },
        ),
    ]
