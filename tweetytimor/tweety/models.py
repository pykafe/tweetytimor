from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Tweety(models.Model):
    description = models.TextField(max_length=1000)
    
