# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='Электронная почта')),
                ('firstname', models.CharField(null=True, max_length=50, verbose_name='Имя/Наименование', blank=True)),
                ('register_date', models.DateField(verbose_name='Дата регистрации', auto_now_add=True)),
                ('mobile', models.CharField(default='', max_length=50, validators=[django.core.validators.RegexValidator('^((8|\\+7)[\\- ]?)?(\\(?\\d{3}\\)?[\\- ]?)?[\\d\\- ]{7,10}$', 'Мобильный телефон имеет неверный формат')], verbose_name='Мобильный телефон')),
                ('skype', models.CharField(default='', max_length=32, verbose_name='Логин Skype')),
                ('user_type', models.CharField(choices=[(0, 'Частное лицо'), (1, 'Компания')], default='Частное лицо', max_length=16, verbose_name='Тип пользователя')),
                ('rate', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Суперпользователь')),
                ('groups', models.ManyToManyField(related_query_name='user', verbose_name='groups', related_name='user_set', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', verbose_name='user permissions', related_name='user_set', blank=True, help_text='Specific permissions for this user.', to='auth.Permission')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
