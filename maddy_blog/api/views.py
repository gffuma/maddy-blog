from rest_framework import serializers, viewsets, views
from rest_framework.generics import get_object_or_404
from rest_framework import filters
from blog.models import Post, Category, Content
from django.http import Http404

# Mixin for lookup with pk or slug
class BySlugOrPkMixin(object):
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        # Try first for pk, then try with slug or fail
        try:
            obj = get_object_or_404(queryset, pk=self.kwargs[lookup_url_kwarg])
        except Http404:
            obj = get_object_or_404(queryset, slug=self.kwargs[lookup_url_kwarg])

        self.check_object_permissions(self.request, obj)
        return obj

# Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        depth = 1

class PostViewSet(BySlugOrPkMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.filter(published=True)
    serializer_class = PostSerializer

# Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

class CategoryViewSet(BySlugOrPkMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('inmenu',)

# Content
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content

class ContentViewSet(BySlugOrPkMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Content.objects.filter(published=True)
    serializer_class = ContentSerializer
