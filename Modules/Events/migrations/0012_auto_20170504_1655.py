# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0011_auto_20170504_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 4, 16, 55, 58, 106000)),
        ),
    ]
