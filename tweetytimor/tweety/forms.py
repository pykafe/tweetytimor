from django import forms
#from tweety.models import TweetyComment


class TweetyCommentForm(forms.Form):
    tweet = forms.CharField(widget=forms.HiddenInput())
    tweetycomment = forms.CharField(widget=forms.TextInput())
