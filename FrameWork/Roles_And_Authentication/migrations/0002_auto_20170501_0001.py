# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Noun', '0001_initial'),
        ('Roles_And_Authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userroles',
            name='allowedNoun',
            field=models.ManyToManyField(to='Noun.Noun'),
        ),
        migrations.AlterField(
            model_name='userroles',
            name='UsersRole',
            field=models.OneToOneField(to='Users_And_Groups.UserProfile'),
        ),
        migrations.RemoveField(
            model_name='userroles',
            name='intendedRoles',
        ),
        migrations.AddField(
            model_name='userroles',
            name='intendedRoles',
            field=models.ManyToManyField(to='Roles_And_Authentication.Roles'),
        ),
    ]
