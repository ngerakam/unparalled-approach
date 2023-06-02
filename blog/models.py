from django.db import models
from user.models import User
from django.utils.text import slugify
from PIL import Image
from tinymce.models import HTMLField


class Author(models.Model):
    name = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    name = models.CharField(max_length=255, blank=True)
    category_post = models.ForeignKey(
        "Post", on_delete=models.SET_NULL, null=True, related_name="+", blank=True
    )

    def __str__(self):
        return str(self.name)


class MediaPost(models.Model):
    MEDIA_PHOTO = "PH"
    MEDIA_VIDEO = "VD"
    MEDIA_DOCUMENT = "DOC"

    MEDIA_CHOICES = [
        (MEDIA_VIDEO, "Video"),
        (MEDIA_PHOTO, "Photo"),
        (MEDIA_DOCUMENT, "Document"),
    ]

    name = models.CharField(max_length=150, blank=True, null=True)
    alt_text = models.CharField(max_length=150, blank=True, null=True)
    media_type = models.CharField(
        max_length=8, choices=MEDIA_CHOICES, default=MEDIA_PHOTO
    )
    video_url = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    document = models.FileField(null=True, blank=True)
    media_post = models.ForeignKey(
        "Post", on_delete=models.SET_NULL, null=True, related_name="+", blank=True
    )

    def save(self, *args, **kwargs):
        # Ensure that only one type of media (image or video) is set
        if self.media_type == "Photo":
            self.video_url = None
            self.document = None

        elif self.media_type == "Video":
            self.video_url = None
            self.document = None
        elif self.media_type == "Document":
            self.video_url = None
            self.image = None
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class RelatedPost(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(blank=True, null=True)
    featured_post = models.ForeignKey(
        "Post", on_delete=models.SET_NULL, null=True, related_name="+", blank=True
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(RelatedPost, self).save(*args, **kwargs)

    def create_thumbnail(self):
        if not self.thumbnail:
            return

        # Open the original image
        original_image = Image.open(self.thumbnail)

        # Resize and save the thumbnail image
        thumbnail_size = (200, 200)
        original_image.thumbnail(thumbnail_size)
        thumbnail_filename = f"thumbnail_{self.thumbnail.name}"
        original_image.save(thumbnail_filename)

        # Update the thumbnail field with the newly created thumbnail
        self.thumbnail = thumbnail_filename

    def __str__(self):
        return str(self.title)


class Post(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.SET_NULL)
    content = HTMLField()
    excerpt = HTMLField(max_length=100, blank=True)
    publication_date = models.DateTimeField(auto_created=True)
    updated_date = models.DateTimeField(auto_now=True)
    reads = models.IntegerField(blank=True, null=True)
    # comments = models.ForeignKey(
    #     Comment, blank=True, null=True, on_delete=models.SET_NULL
    # )
    media = models.ForeignKey(
        MediaPost, blank=True, null=True, on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        Category, blank=True, null=True, on_delete=models.SET_NULL
    )
    related_post = models.ForeignKey(
        RelatedPost, blank=True, null=True, on_delete=models.SET_NULL
    )
    post_comment = models.ForeignKey(
        "Post", on_delete=models.SET_NULL, null=True, related_name="+", blank=True
    )

    class Meta:
        ordering = ["-publication_date"]

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    text = HTMLField()
    comment_date = models.DateTimeField(auto_created=True)
    post = models.ForeignKey(
        Post, on_delete=models.SET_NULL, null=True, related_name="+", blank=True
    )

    class Meta:
        ordering = ["-comment_date"]

    def __str__(self):
        return str(self.name)
