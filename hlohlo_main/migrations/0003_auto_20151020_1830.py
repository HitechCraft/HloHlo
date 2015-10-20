# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0002_auto_20151020_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('desription', models.TextField(verbose_name='Описание')),
                ('subcategory', models.ForeignKey(to='hlohlo_main.Category')),
            ],
        ),
        migrations.AlterModelOptions(
            name='lot',
            options={'verbose_name_plural': 'Лоты', 'verbose_name': 'лот'},
        ),
    ]
