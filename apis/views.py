from django.shortcuts import render
from rest_framework import viewsets
from apis.serializers import PostSerializer, ProfileSerializer
from .permissions import IsAuthorOrReadOnly
from posts.models import Post
from profiles.models import Profile 
# Create your views here.
# Create your views here.


class PostViewSet(viewsets.ModelViewSet): 

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    owner = 'author'

class ProfileViewSet(viewsets.ModelViewSet): 

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    owner = 'user'