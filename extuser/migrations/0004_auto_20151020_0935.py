# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extuser', '0003_auto_20151020_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extuser',
            name='firstname',
            field=models.CharField(null=True, verbose_name='Имя/Наименование', max_length=50, blank=True),
        ),
    ]
