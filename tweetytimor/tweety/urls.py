from django.conf.urls import url
from .views import TweetyCreate, LikeTweet, TweetComment, CreateMember


urlpatterns = [
    url(r'^$', TweetyCreate.as_view(), name='tweety'),
    url(r'^create/$', CreateMember.as_view(), name='create'),
    url(r'^like', LikeTweet.as_view(), name='like'),
    url(r'^comment', TweetComment.as_view(), name='comment'),
]
