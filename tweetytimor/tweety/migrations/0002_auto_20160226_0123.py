# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweety', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetytimor',
            name='comment',
            field=models.TextField(max_length=1000, null=True, blank=True),
        ),
    ]
