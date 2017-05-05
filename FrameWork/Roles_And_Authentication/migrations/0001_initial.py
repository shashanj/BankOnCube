# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roleCode', models.CharField(max_length=100)),
                ('title', models.CharField(default=b'', max_length=100, blank=True)),
                ('description', models.CharField(default=b'', max_length=100, blank=True)),
                ('isActive', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='UserRoles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('UsersRole', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('intendedRoles', models.ForeignKey(to='Roles_And_Authentication.Roles')),
            ],
        ),
    ]
