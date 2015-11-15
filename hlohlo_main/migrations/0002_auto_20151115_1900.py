# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hlohlo_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(max_length=1500, verbose_name='Описание', blank=True)),
                ('sub_category', models.ManyToManyField(to='hlohlo_main.Category', null=True, blank=True, related_name='_sub_category_+')),
            ],
            options={
                'verbose_name_plural': 'категории лотов',
                'verbose_name': 'категории лотов',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'города',
                'verbose_name': 'город',
            },
        ),
        migrations.CreateModel(
            name='CityDistrict',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'районы',
                'verbose_name': 'район',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name_plural': 'коллекции лотов',
                'verbose_name': 'коллекция лотов',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('file', models.ImageField(upload_to='images', verbose_name='Фото', help_text='Форматы: png, jpg, jpeg, bmp. gif')),
            ],
            options={
                'verbose_name_plural': 'Фото',
                'verbose_name': 'Фото',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('cities', models.ManyToManyField(to='hlohlo_main.City')),
            ],
            options={
                'verbose_name_plural': 'регионы',
                'verbose_name': 'регион',
            },
        ),
        migrations.AlterModelOptions(
            name='lot',
            options={'verbose_name_plural': 'лоты', 'verbose_name': 'лот'},
        ),
        migrations.RemoveField(
            model_name='lot',
            name='Author',
        ),
        migrations.RemoveField(
            model_name='lot',
            name='Buyer',
        ),
        migrations.AddField(
            model_name='lot',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='author_profile', default=''),
        ),
        migrations.AddField(
            model_name='lot',
            name='buyer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='buyer_profile', default=''),
        ),
        migrations.AlterField(
            model_name='lot',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='lot',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='lot',
            name='time_life',
            field=models.IntegerField(verbose_name='Время на аукцион (в днях)'),
        ),
        migrations.AddField(
            model_name='photo',
            name='lot',
            field=models.ForeignKey(to='hlohlo_main.Lot', default='', verbose_name='Лот'),
        ),
        migrations.AddField(
            model_name='collection',
            name='lots',
            field=models.ManyToManyField(to='hlohlo_main.Lot', verbose_name='Лот'),
        ),
        migrations.AddField(
            model_name='city',
            name='cityDistricts',
            field=models.ManyToManyField(to='hlohlo_main.CityDistrict'),
        ),
        migrations.AddField(
            model_name='lot',
            name='category',
            field=models.ManyToManyField(to='hlohlo_main.Category'),
        ),
    ]
