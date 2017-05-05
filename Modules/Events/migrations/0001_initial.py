# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import Core.JSONField
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Verb', '0001_initial'),
        ('Noun', '0001_initial'),
        ('Users_And_Groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ts', models.CharField(max_length=15)),
                ('latlong', models.CharField(max_length=15)),
                ('timespent', models.IntegerField()),
                ('properties', Core.JSONField.JSONField(null=True, blank=True)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2017, 5, 1, 0, 1, 10, 148000))),
                ('noun', models.ForeignKey(to='Noun.Noun')),
                ('user_id', models.ForeignKey(to='Users_And_Groups.UserProfile')),
                ('verb', models.ForeignKey(to='Verb.Verb')),
            ],
        ),
    ]
