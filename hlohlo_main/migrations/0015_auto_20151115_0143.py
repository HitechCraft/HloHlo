# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0014_auto_20151115_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Альбомы',
                'verbose_name': 'Альбом',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('file', models.ImageField(help_text='Желательно, чтоб фото было не большого размера', upload_to='images', verbose_name='Фото')),
                ('album', models.ForeignKey(to='hlohlo_main.Album')),
            ],
            options={
                'verbose_name_plural': 'Фото',
                'verbose_name': 'Фото',
            },
        ),
        migrations.AddField(
            model_name='lot',
            name='album',
            field=models.OneToOneField(default='', to='hlohlo_main.Album'),
        ),
    ]
