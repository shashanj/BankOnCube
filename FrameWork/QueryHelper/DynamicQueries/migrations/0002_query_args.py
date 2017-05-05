# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DynamicQueries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='args',
            field=models.TextField(default='user_id'),
            preserve_default=False,
        ),
    ]
