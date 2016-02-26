from django.forms import ModelForm
from .models import TweetyLike


class LikeForm(ModelForm):
    class Meta:
        model = TweetyLike
        fields = ['like']
