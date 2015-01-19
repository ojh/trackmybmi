# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='height',
            field=models.DecimalField(help_text='Height in metres', decimal_places=2, max_digits=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='measurement',
            name='weight',
            field=models.DecimalField(help_text='Mass in kilograms', decimal_places=2, max_digits=5),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='measurement',
            unique_together=set([('user', 'date')]),
        ),
    ]
