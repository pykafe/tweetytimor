from __future__ import unicode_literals

from django.db import models


class TweetyTimor(models.Model):

    NATION_CHOICES = (
            ('', 'All Country'),
            ('timor-leste', 'Timor-Leste'),
            ('usa', 'USA'),
            ('england', 'England'),
            ('australia', 'Australia'),
            )

    comment = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)
    nation = models.CharField(max_length = 20, choices = NATION_CHOICES, help_text = "Select your country", null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, help_text="Select your image")


class TweetyLike(models.Model):

    like = models.EmailField(max_length=254)
