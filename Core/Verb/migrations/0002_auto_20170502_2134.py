# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Verb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verb',
            name='id',
        ),
        migrations.AlterField(
            model_name='verb',
            name='verb_code',
            field=models.CharField(max_length=10, serialize=False, primary_key=True),
        ),
    ]
