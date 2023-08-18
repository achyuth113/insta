from __future__ import absolute_import

from django.urls import path, re_path

from .views import *
from .rest_views import *

urlpatterns = [
    re_path(r'feed/$', NewsFeed.as_view(), name='feed'),
    re_path(r'create/$',CreatePostView.as_view(),name='add_post'),
    re_path(r'(?P<pk>\d+)/(?P<slug>\d+)/$',DetailPostView.as_view(),name='view'),
    re_path(r'(?P<pk>\d+)/edit/$',EditPost.as_view(), name="edit_post"),
    re_path(r'(?P<pk>\d+)/delete/$', DeletePost.as_view(), name="delete_post"),
    path('<int:pk>/likes', LikesList, name="post_likes"),
    path('<int:pk>/comment', addComment, name="post_add_comment"),
    path('likes/api/', LikesListApi.as_view(), name="user_likes_api"),
    path('like/<int:post_id>', LikesToggle.as_view(), name="like_toggle"),
]
