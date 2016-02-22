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
            name='nation',
            field=models.CharField(blank=True, max_length=20, null=True, help_text='Select your country', choices=[('', 'All Country'), ('timor-leste', 'Timor-Leste'), ('usa', 'USA'), ('england', 'England'), ('australia', 'Australia')]),
        ),
        migrations.AlterField(
            model_name='tweetytimor',
            name='photo',
            field=models.ImageField(help_text='Select your image', null=True, upload_to=b'', blank=True),
        ),
    ]
