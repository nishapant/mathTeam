from django.conf.urls import url
from . import views

app_name = 'core'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post_list/$', views.post_list, name='post_list'),
    url(r'^question_list/$', views.question_list, name ='question_list'),
    url(r'^question_list/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
]
