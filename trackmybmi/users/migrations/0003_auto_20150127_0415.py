# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_friendship'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friendship',
            old_name='is_confirmed',
            new_name='is_accepted',
        ),
    ]
