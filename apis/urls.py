from django.urls import path, include
from rest_framework.routers import SimpleRouter

from apis.views import *



router = SimpleRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('profiles', ProfileViewSet, basename='profiles')

urlpatterns = router.urls