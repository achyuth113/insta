from django.urls import path, re_path
from .views import *
from .rest_views import *
app_name = "users"

urlpatterns = [
    re_path(r'^signup/$', SignupView.as_view(), name='signup_form'),
    re_path(r'^login/$', LoginView.as_view(), name='login_form'),
    re_path(r'profile/(?P<pk>\d+)/$', DetailAccountView.as_view(), name='profile'),
    re_path(r'^logout/$', LogOutView.as_view(), name='logout_form'),
    re_path(r'users_list/(?P<pk>\d+)/$',ListAccountView.as_view(),name='user_list'),
    re_path(r'update/(?P<pk>\d+)/$',UpdateAccountView.as_view(),name='update'),
    re_path(r'update/password/(?P<pk>\d+)/$',change_password,name='change_password'),
    re_path(r'followers/(?P<pk>\d+)/$',FollowersListView.as_view(),name='followers'),
    re_path(r'following/(?P<pk>\d+)/$',FollowingListView.as_view(),name='following'),
    re_path(r'follow/(?P<pk>\d+)/$',follow_view,name='follow'),
    re_path(r'(?P<pk>\d+)/unfollow/$',unfollow_view,name='unfollow'),
    path('users/api/<slug:slug>', SearchApi.as_view(), name="search_api"),
]

