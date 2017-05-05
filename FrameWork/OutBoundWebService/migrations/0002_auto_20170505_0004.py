# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OutBoundWebService', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bc_fw_config_var_b',
            old_name='pror_value',
            new_name='prop_value',
        ),
    ]
