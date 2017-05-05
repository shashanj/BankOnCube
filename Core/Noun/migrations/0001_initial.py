# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Verb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification_Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notification_enable', models.CharField(max_length=3, choices=[(b'0', b'true'), (b'1', b'false'), (b'2', b'condtional')])),
                ('expected_output_type', models.CharField(max_length=100)),
                ('expected_output', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Noun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('noun_code', models.CharField(max_length=10)),
                ('noun', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=100)),
                ('allowedVerb', models.ManyToManyField(to='Verb.Verb')),
            ],
        ),
        migrations.AddField(
            model_name='notification_config',
            name='noun',
            field=models.ForeignKey(to='Noun.Noun'),
        ),
        migrations.AddField(
            model_name='notification_config',
            name='verb',
            field=models.ForeignKey(to='Verb.Verb'),
        ),
    ]
