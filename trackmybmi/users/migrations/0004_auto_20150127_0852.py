# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150127_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendship',
            name='is_accepted',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='friendship',
            name='is_active',
            field=models.BooleanField(default=True, editable=False),
            preserve_default=True,
        ),
    ]
