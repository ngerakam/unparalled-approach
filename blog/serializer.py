from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    # category_post = serializers.ReadOnlyField(source="category_post.id")

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
        ]


class MediaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaPost
        fields = [
            "id",
            "name",
            "alt_text",
            "video_url",
            "image",
            "document",
            "media_post",
            "media_type",
        ]


class RelatedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedPost
        fields = [
            "id",
            "title",
            "slug",
            "thumbnail",
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "name",
            "text",
            "comment_date",
        ]

        def create(self, validated_data):
            post_id = self.context["post_id"]
            return Comment.objects.create(post_id=post_id, **validated_data)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.name.username")

    class Meta:
        model = Post
        depth = 1
        fields = [
            "id",
            "title",
            "slug",
            "author",
            "content",
            "excerpt",
            "publication_date",
            "updated_date",
            "reads",
            "media",
            "category",
            "related_post",
        ]
