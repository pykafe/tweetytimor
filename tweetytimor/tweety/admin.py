from django.contrib import admin

# Register your models here.
from tweety.models import PersonTweety
from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS
from webcam import widgets
from webcam.fields import CameraField


FORMFIELD_FOR_DBFIELD_DEFAULTS[CameraField] = {'widget': widgets.CameraWidget}


admin.site.register(PersonTweety)
