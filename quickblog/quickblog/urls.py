"""quickblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
'''
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]
'''

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import posts.views

urlpatterns = patterns('',

    url(r'^list/$', posts.views.ListPostView.as_view(),
        name='posts-list',),
    url(r'^add/$', posts.views.CreatePostView.as_view(),
        name='post-new',),
    url(r'^edit/(?P<pk>\d+)/$',posts.views.UpdatePostView.as_view(),
        name='post-edit',),
    url(r'^delete/(?P<pk>\d+)/$',posts.views.DeletePostView.as_view(),
        name='post-delete',),
    url(r'^(?P<pk>\d+)/$', posts.views.PostDetailView.as_view(),
        name='post-detail',),
    url(r'^register/$', posts.views.register, name='register'),
    url(r'^login/$', posts.views.user_login, name='login'),
    url(r'^logout/$', posts.views.user_logout, name='logout'),

    url(r'^$', posts.views.ListPostView.as_view(), name='index'),
    url(r'^managepostlist/$', posts.views.managepostlist, name='managepostlist'),
    url(r'^(?P<post_id>\d+)/upvote/$',posts.views.upvote, name='upvote'),

)
urlpatterns += staticfiles_urlpatterns()
