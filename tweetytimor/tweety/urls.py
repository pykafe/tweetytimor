from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import TweetyCreate, LikeTweet, TweetComment, CreateMember


urlpatterns = [
    url(r'^$', TweetyCreate.as_view(), name='tweety'),
    url(r'^create/$', login_required(CreateMember.as_view()), name='create'),
    url(r'^like', LikeTweet.as_view(), name='like'),
    url(r'^comment', TweetComment.as_view(), name='comment'),
]
