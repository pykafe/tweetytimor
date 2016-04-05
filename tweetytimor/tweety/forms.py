from django.forms import ModelForm
from .models import TweetyLike, TweetyUser, PersonTweety
from django.core.exceptions import ValidationError
from django import forms


class LikeForm(ModelForm):
    class Meta:
        model = TweetyLike
        fields = ['like']


class PersonForm(ModelForm):
    class Meta:
        model = PersonTweety
        fields = ['picture',]

class RegisterUser(ModelForm):
    class Meta:
        model = TweetyUser
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'confirm_email']
        widgets = {'password': forms.PasswordInput()}

    def clean(self):
        if (self.cleaned_data.get('email') != self.cleaned_data.get('confirm_email')):
            raise ValidationError("Email addresses must match.")
        return self.cleaned_data
