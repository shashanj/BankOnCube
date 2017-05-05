# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Noun', '0003_auto_20170502_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification_config',
            name='noun',
        ),
        migrations.RemoveField(
            model_name='notification_config',
            name='verb',
        ),
        migrations.DeleteModel(
            name='Notification_Config',
        ),
    ]
