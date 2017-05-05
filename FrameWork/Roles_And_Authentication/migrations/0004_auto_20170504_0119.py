# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Roles_And_Authentication', '0003_auto_20170503_2209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userroles',
            old_name='UsersRole',
            new_name='usersRole',
        ),
    ]
