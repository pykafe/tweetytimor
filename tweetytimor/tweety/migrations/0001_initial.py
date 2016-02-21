# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TweetyLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('like', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TweetyTimor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(max_length=1000)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('nation', models.CharField(help_text='Select your country', max_length=20, choices=[('', 'All Country'), ('timor-leste', 'Timor-Leste'), ('usa', 'USA'), ('england', 'England'), ('australia', 'Australia')])),
            ],
        ),
    ]
