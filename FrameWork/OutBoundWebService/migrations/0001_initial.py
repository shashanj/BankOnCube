# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BC_FW_CONFIG_VAR_B',
            fields=[
                ('prop_id', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('pror_value', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('desc', models.TextField()),
            ],
        ),
    ]
