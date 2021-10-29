from django.urls import path, include
from profiles.views import (
ProfileDetailView, NotificationListView,
ProfileListView,ProfileEditView,add_remove_friend, friend_request,
accept_reject_request, search)

app_name = 'profile'
urlpatterns = [

    path('profile-detail/<int:pk>', ProfileDetailView.as_view(), name='profile-detail'),
    path('friends', ProfileListView.as_view(), name='friends'),
    path('profile-edit/<int:pk>', ProfileEditView.as_view(), name='profile-edit'),
    path('friend-request', friend_request, name='friend-request'),
    path('notification-list',  NotificationListView.as_view(),  name='notification-list'),
    path('add-remove-friend', add_remove_friend, name='add-remove-friend'),
    path('accept-reject-request',accept_reject_request, name='accept-reject-request'),
    path('search', search,name = 'search'),
    
]