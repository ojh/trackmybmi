# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150127_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendship',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('ACTIVE', 'Active'), ('REJECTED', 'Rejected'), ('ENDED', 'Ended')], max_length=30, default='PENDING', editable=False),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together=set([('initiator', 'recipient')]),
        ),
        migrations.RemoveField(
            model_name='friendship',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='friendship',
            name='is_accepted',
        ),
    ]
