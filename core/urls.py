from django.urls import path, include


urlpatterns = [
    # articles
    path("", include("blog.urls")),
]
