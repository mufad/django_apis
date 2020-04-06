from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

    # /posts/
    path('', views.index, name='index'),

    # /posts/1
    url(r'^(?P<post_id>[0-9]+)$', views.post_details, name="post_details"),
]
