from django.conf.urls import url, include
from tweety import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name="index"),
    url(r'^like/$', views.Like.as_view(), name="like"),
    url(r'^create/$', views.CreateTweetyUser.as_view(), name="create"),
]
