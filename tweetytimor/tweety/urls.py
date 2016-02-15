from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = patterns(
    '',
    url(r'^$', login_required(views.Home.as_view()), name='home'),
    )
