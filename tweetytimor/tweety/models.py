from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models


class TweetyTimor(models.Model):
    comment = models.TextField(max_length=200)


class Like(models.Model):
    tweet = models.ForeignKey(TweetyTimor)


class TweetComment(models.Model):
    tweet = models.ForeignKey(TweetyTimor)
    tweetcomment = models.TextField(max_length=200)


class Member(AbstractUser):
    ''' model containing details about a member '''
    job_title = models.CharField(max_length=250)
    bio_text = models.TextField(max_length=1000)
