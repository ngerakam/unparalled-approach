from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet


from .models import UserProfile
from .serializer import UserProfileSerializer


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    # @action(detail=False)
    # def me(self, request):
    #     user_profile = UserProfile.objects.get(user=request.user.id)
    #     serializer = UserProfileSerializer(user_profile)
    #     return Response(serializer.data)

    def get_serializer_context(self):
        return {"request": self.request}

    def destroy(self, request, pk):
        users_profile = get_object_or_404(UserProfile, user_id=pk)
        users_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
