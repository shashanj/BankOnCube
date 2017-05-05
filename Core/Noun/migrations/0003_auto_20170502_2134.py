# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Noun', '0002_notification_config_condition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noun',
            name='id',
        ),
        migrations.AlterField(
            model_name='noun',
            name='noun_code',
            field=models.CharField(max_length=10, serialize=False, primary_key=True),
        ),
    ]
