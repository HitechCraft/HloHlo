# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extuser', '0002_remove_extuser_middlename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extuser',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='extuser',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='extuser',
            name='lastname',
        ),
        migrations.AlterField(
            model_name='extuser',
            name='firstname',
            field=models.CharField(null=True, blank=True, max_length=40, verbose_name='Имя/Наименование'),
        ),
    ]
