from django.conf.urls import url, include
from rest_framework import routers
from .views import PostViewSet, CategoryViewSet, ContentViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'contents', ContentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
