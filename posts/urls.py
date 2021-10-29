from django.urls import path, include
from posts.views import (PostCreateView, 
                        add_comments,
                        add_remove_likes,
                        PostUpdateView,
                        PostDeleteView,PostDetailView)
app_name='post'
urlpatterns = [
    path('', PostCreateView.as_view() , name= 'new-post'),
    path('<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('add-remove-likes',add_remove_likes, name='add-remove-likes'),
    path('add-comments', add_comments, name='new-comment'),

]