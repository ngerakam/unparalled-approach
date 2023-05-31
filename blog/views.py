from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *
from .pagination import DefaultPagination


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # filter_backends = [DjangoFilterBackend]
    # pagination_class = DefaultPagination

    def get_serializer_context(self):
        return {"request": self.request}

    def destroy(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = DefaultPagination

    def get_serializer_context(self):
        return {"request": self.request}

    def destroy(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MediaPostViewSet(ModelViewSet):
    queryset = MediaPost.objects.all()
    serializer_class = MediaPostSerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = DefaultPagination

    def get_serializer_context(self):
        return {"request": self.request}

    def destroy(self, request, pk):
        media = get_object_or_404(MediaPost, pk=pk)
        media.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RelatedPostViewSet(ModelViewSet):
    queryset = RelatedPost.objects.all()
    serializer_class = RelatedPostSerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = DefaultPagination

    def get_serializer_context(self):
        return {"request": self.request}

    def destroy(self, request, pk):
        rpost = get_object_or_404(RelatedPost, pk=pk)
        rpost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get("post_pk")
        return Comment.objects.filter(post_id=post_id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        post_id = self.kwargs.get("post_pk")
        context["post_id"] = post_id
        return context
