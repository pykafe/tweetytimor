from __future__ import unicode_literals

from django.db import models


class TweetyTimor(models.Model):
    comment = models.TextField(max_length=200)

    def __unicode__(self):
        return self.comment


class LikeTweet(models.Model):
    tweet = models.ForeignKey(TweetyTimor)


class TweetComment(models.Model):
    tweet = models.ForeignKey(TweetyTimor)
    comment = models.TextField(max_length=200)
