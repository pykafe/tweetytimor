from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

import webcam
import tempfile
import webcam.admin

#from webcam.fields import DBCameraField, FSCameraField
#from webcam.storage import CameraFileSystemStorage
from webcam.fields import CameraField


class PersonTweety(models.Model):
    picture = CameraField()

    def __str__(self):
        return (' %s' % self.picture).encode('ascii', errors='replace')
   # picture1 = DBCameraField() # store in the database
   # picture2 = FSCameraField(format='gif', max_length=100) # by default storen on settings.MEDIA_ROOT
    #picture3 = FSCameraField(format='png', storage=CameraFileSystemStorage('/absolute/path/to/'), null=True, blank=True) # store on filesystem


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
    nation = models.CharField(max_length=20, choices=NATION_CHOICES, help_text="Select your country", null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, help_text="Select your image")


class TweetyLike(models.Model):

    like = models.EmailField(max_length=254, unique=True)


class TweetyUser(AbstractUser):
    confirm_email = models.EmailField(max_length=254, unique=True, help_text="confirm your email")
