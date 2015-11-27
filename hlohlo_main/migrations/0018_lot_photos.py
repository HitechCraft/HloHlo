# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlohlo_main', '0017_collection_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='photos',
            field=models.FileField(upload_to='attachments', default=''),
            preserve_default=False,
        ),
    ]
