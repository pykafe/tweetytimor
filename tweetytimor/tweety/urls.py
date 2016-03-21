from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^tweety_update/(?P<pk>\d+)/$', login_required(views.TweetyUpdate.as_view()), name='tweety_update'),
    url(r'^tweety_delete/(?P<pk>\d+)/$', login_required(views.TweetyDelete.as_view()), name='tweety_delete'),
]
