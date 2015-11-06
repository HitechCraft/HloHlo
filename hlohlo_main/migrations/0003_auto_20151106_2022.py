# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0002_auto_20151020_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CityDistrict',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Lots',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название', max_length=255)),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название', max_length=255)),
                ('cities', models.ForeignKey(to='hlohlo_main.City')),
            ],
        ),
        migrations.AlterModelOptions(
            name='lot',
            options={'verbose_name_plural': 'лоты', 'verbose_name': 'лот'},
        ),
        migrations.AddField(
            model_name='lots',
            name='lots',
            field=models.ForeignKey(to='hlohlo_main.Lot'),
        ),
        migrations.AddField(
            model_name='city',
            name='cityDistricts',
            field=models.ForeignKey(to='hlohlo_main.CityDistrict'),
        ),
    ]
