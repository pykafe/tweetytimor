from django.conf.urls import url, patterns
from tweety import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name="index"),
    url(r'^like/$', views.Like.as_view(), name="like"),
    url(r'^create/$', views.CreateTweetyUser.as_view(), name="create"),
    url(r'^persontweety/$', views.Person.as_view(), name="persontweety"),
    url(r'^edit/(?P<pk>\d+)/$', views.UpdateTweety.as_view(), name="edit"),
]
