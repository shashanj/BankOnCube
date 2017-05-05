# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('modelName', models.CharField(max_length=100)),
                ('filters', models.TextField()),
                ('desc', models.TextField()),
            ],
        ),
    ]
