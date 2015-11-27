# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('extuser', '0002_auto_20151115_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('file', models.ImageField(help_text='Форматы: png, jpg, jpeg, bmp. gif', upload_to='images/avatars', verbose_name='Аватар')),
                ('user', models.ForeignKey(default='', verbose_name='Пользователь', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
