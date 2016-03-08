# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweety', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetytimor',
            name='name',
            field=models.TextField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
