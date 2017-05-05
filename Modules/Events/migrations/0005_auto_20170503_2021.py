# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0004_auto_20170503_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 20, 21, 35, 45000)),
        ),
        migrations.AlterField(
            model_name='event',
            name='noun',
            field=models.ForeignKey(blank=True, to='Noun.Noun', null=True),
        ),
    ]
