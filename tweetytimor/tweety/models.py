from __future__ import unicode_literals

from django.db import models


class TweetyTimor(models.Model):
    comment = models.TextField(max_length=400)
