# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweety', '0002_auto_20160215_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetytimor',
            name='comment',
            field=models.TextField(max_length=100),
        ),
    ]
