# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Noun', '0003_auto_20170502_2134'),
        ('Roles_And_Authentication', '0002_auto_20170501_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userroles',
            name='allowedNoun',
        ),
        migrations.AddField(
            model_name='roles',
            name='allowedNoun',
            field=models.ManyToManyField(to='Noun.Noun'),
        ),
    ]
