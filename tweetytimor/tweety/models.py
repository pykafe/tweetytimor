from __future__ import unicode_literals

from django.db import models


class TweetyTimor(models.Model):
    comment = models.TextField(max_length=225)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.comment


class Like(models.Model):
    tweety = models.ForeignKey(TweetyTimor)


class TweetyComment(models.Model):
    tweet = models.ForeignKey(TweetyTimor)
    tweetycomment = models.TextField(max_length=225)

    def __unicode__(self):
        return self.comment
