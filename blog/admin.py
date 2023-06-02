from django.contrib import admin
from user.models import User
from .models import *


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    autocomplete_fields = [
        "name",
    ]
    list_display = [
        "name",
        "email",
        
        "post_count",
    ]
    search_fields = [
        "name__istartswith",
    ]
    list_per_page = 10
    ordering = [
        "name",
    ]

    def post_count(self, author):
        count = Post.objects.filter(author=author).count()
        return count

    def email(self, author):
        return author.name.email

    def phone_number(self, author):
        return author.name


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    autocomplete_fields = [
        "category_post",
    ]
    list_display = [
        "name",
    ]
    search_fields = [
        "name__istartswith",
    ]
    list_per_page = 10


@admin.register(MediaPost)
class MediaPostAdmin(admin.ModelAdmin):
    autocomplete_fields = [
        "media_post",
    ]
    list_display = [
        "name",
        "media_type",
        "alt_text",
    ]
    search_fields = [
        "name__istartswith",
    ]
    list_per_page = 10


@admin.register(RelatedPost)
class RelatedPostAdmin(admin.ModelAdmin):
    autocomplete_fields = [
        "featured_post",
    ]

    prepopulated_fields = {
        "slug": ["title"],
    }
    list_display = [
        "title",
        "slug",
    ]
    search_fields = [
        "title__istartswith",
    ]
    list_per_page = 10


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    autocomplete_fields = [
        "media",
        "category",
        "related_post",
        "post_comment",
        "author",
    ]
    prepopulated_fields = {
        "slug": ["title"],
    }
    list_display = [
        "title",
        "author_name",
        "category_title",
        "publication_date",
        "updated_date",
        "reads_count",
        "comments_no",
        "media_count",
    ]
    list_per_page = 15

    search_fields = [
        "title__istartswith",
    ]
    ordering = [
        "reads",
    ]

    def author_name(self, post):
        return post.author.name.username

    def reads_count(self, post):
        return post.reads

    def category_title(self, post):
        return post.category

    def comments_no(self, post):
        count = Comment.objects.filter(post=post.id).count()
        return count

    def media_count(self, post):
        count = MediaPost.objects.filter(id=post.media.id).count()
        return count


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "comment_date",
    ]
    list_per_page = 15
    autocomplete_fields = [
        "post",
    ]
