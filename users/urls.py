from django.urls import path
from django.conf.urls import url
from .views import *
from .rest_views import *
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm
app_name = "users"

urlpatterns = [
    url(r'^signup/$', SignupView.as_view(), name='signup_form'),
    url(r'^login/$', LoginView.as_view(), name='login_form'),
    url(r'profile/(?P<pk>\d+)/$', DetailAccountView.as_view(), name='profile'),
    url(r'^logout/$', LogOutView.as_view(), name='logout_form'),
    url(r'users_list/(?P<pk>\d+)/$',ListAccountView.as_view(),name='user_list'),
    url(r'update/(?P<pk>\d+)/$',UpdateAccountView.as_view(),name='update'),
    url(r'update/password/(?P<pk>\d+)/$',change_password,name='change_password'),
    url(r'followers/(?P<pk>\d+)/$',FollowersListView.as_view(),name='followers'),
    url(r'following/(?P<pk>\d+)/$',FollowingListView.as_view(),name='following'),
    url(r'follow/(?P<pk>\d+)/$',follow_view,name='follow'),
    url(r'(?P<pk>\d+)/unfollow/$',unfollow_view,name='unfollow'),
    path('users/api/<slug:slug>', SearchApi.as_view(), name="search_api"),
]

