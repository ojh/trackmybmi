# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('initiator', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='outgoing_friendships', related_query_name='outgoing_friendship')),
                ('recipient', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='incoming_friendships', related_query_name='incoming_friendship')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
