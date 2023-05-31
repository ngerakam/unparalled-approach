from django.urls import path, include
from rest_framework_nested import routers
from .views import *
from user.views import UserProfileViewSet

router = routers.DefaultRouter()
router.register("posts", PostViewSet)
router.register("category", CategoryViewSet)
router.register("media", MediaPostViewSet)
router.register("related-post", RelatedPostViewSet)

######userprofile
router.register("profile", UserProfileViewSet)

posts_router = routers.NestedDefaultRouter(router, "posts", lookup="posts")
posts_router.register("comments", CommentViewSet, basename="post-comments")


urlpatterns = [
    path(r"", include(router.urls)),
    path(r"", include(posts_router.urls)),
]
