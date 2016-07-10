from django.conf.urls import url, include

from . import views
from django.views.generic import TemplateView




urlpatterns = [

    url(r'^$', views.home),
    url(r'^home/$', views.after_login),
    url(r'^candidates/$', views.index),
    url(r'^vote/$', views.vote),
    url(r'^vote/polls/(?P<poll_id>\d+)/$', views.polls),
    url(r'^vote/polls/\d+/results/$', views.results),
    url(r'^login/$', views.login),
    url(r'^login/validate/$', views.login_validate),
    url(r'^signup/$', views.signup)


]
