# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweety', '0002_tweetytimor_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='TweetyComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweetycomment', models.TextField(max_length=225)),
            ],
        ),
        migrations.RemoveField(
            model_name='tweetytimor',
            name='name',
        ),
        migrations.AddField(
            model_name='tweetycomment',
            name='tweet',
            field=models.ForeignKey(to='tweety.TweetyTimor'),
        ),
        migrations.AddField(
            model_name='like',
            name='tweety',
            field=models.ForeignKey(to='tweety.TweetyTimor'),
        ),
    ]
