# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('email', models.EmailField(unique=True, verbose_name='Электронная почта', db_index=True, max_length=255)),
                ('avatar', models.ImageField(upload_to='user/avatar', null=True, verbose_name='Аватар', blank=True)),
                ('firstname', models.CharField(null=True, verbose_name='Фамилия', max_length=40, blank=True)),
                ('lastname', models.CharField(null=True, verbose_name='Имя', max_length=40, blank=True)),
                ('middlename', models.CharField(null=True, verbose_name='Отчество', max_length=40, blank=True)),
                ('date_of_birth', models.DateField(null=True, verbose_name='Дата рождения', blank=True)),
                ('register_date', models.DateField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('is_active', models.BooleanField(verbose_name='Активен', default=True)),
                ('is_admin', models.BooleanField(verbose_name='Суперпользователь', default=False)),
                ('groups', models.ManyToManyField(blank=True, verbose_name='groups', related_name='user_set', to='auth.Group', related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.')),
                ('user_permissions', models.ManyToManyField(blank=True, verbose_name='user permissions', related_name='user_set', to='auth.Permission', related_query_name='user', help_text='Specific permissions for this user.')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
