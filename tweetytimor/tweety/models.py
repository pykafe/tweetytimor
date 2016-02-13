from __future__ import unicode_literals

from django.db import models


class TweetyTimor(models.Model):

    comment = models.TextField(max_length=5000)
    created_on = models.DateTimeField(auto_now_add=True)
