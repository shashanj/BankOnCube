# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Verb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('verb_code', models.CharField(max_length=10)),
                ('verb', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
    ]
