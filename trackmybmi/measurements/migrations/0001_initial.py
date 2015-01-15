# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date', models.DateField()),
                ('height', models.DecimalField(max_digits=3, decimal_places=2)),
                ('weight', models.DecimalField(max_digits=5, decimal_places=2)),
                ('user', models.ForeignKey(related_query_name='measurement', to=settings.AUTH_USER_MODEL, related_name='measurements')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
