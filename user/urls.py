from django.urls import path, include
from rest_framework_nested import routers
from .views import *

router = routers.DefaultRouter()
router.register("profile", UserProfileViewSet)

urlpatterns = [
    path(r"", include(router.urls)),
]
