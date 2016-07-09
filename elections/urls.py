from django.conf.urls import url, include

from . import views
from django.views.generic import TemplateView




urlpatterns = [

    url(r'^$', views.home),
    url(r'^home/$', views.home),
    url(r'^candidates/$', views.index),
    url(r'^vote/$', views.vote),
    url(r'^vote/polls/(?P<poll_id>\d+)/$', views.polls),
    url(r'^vote/polls/\d+/results/$', views.results),
    url(r'^signup/$', views.signup),
    url(r'^signup_ok/$', TemplateView.as_view(template_name='log/signup_ok.html'), name='signup_ok')

]
