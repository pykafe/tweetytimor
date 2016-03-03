# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 07:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweety', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TweetComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='tweetytimor',
            name='comment',
            field=models.TextField(max_length=200),
        ),
        migrations.AddField(
            model_name='tweetcomment',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweety.TweetyTimor'),
        ),
        migrations.AddField(
            model_name='like',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweety.TweetyTimor'),
        ),
    ]
