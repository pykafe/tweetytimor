from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

class TweetyTimor(models.Model):

    comment = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(null=True, blank=True)
