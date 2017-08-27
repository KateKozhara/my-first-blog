from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.KateK, name='KateK'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]