from blogApp.models import Articles
from rest_framework import generics, permissions
from .serializers import ArticleSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate
from user import User

from django.db import IntegrityError
from rest_framework.authtoken.models import Token

################# Api part  #################

###### signup and Login using the Api  function based views ###########


@csrf_exempt
def signup(request):
    if request.method == "POST":
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(
                username=data["username"],
                email=data["email"],
                password=data["password"],
            )
            user.save()

            token = Token.objects.create(user=user)

            return JsonResponse({"token": str(token)}, status=201)

        except IntegrityError:
            return JsonResponse({"Error": "Check the data inserted"})


@csrf_exempt
def login(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        user = authenticate(username=data["username"], password=data["password"])

        if user is None:
            return JsonResponse(
                {"Error": "Check the username and password"}, status=400
            )

        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)

        return JsonResponse({"token": str(token)}, status=200)


class ArticleList(generics.ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # I want to override through a function the manual input
    #  of a user or author through the API
    # naming convention as_per below (perform_create) function

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)


########
#### updating and deleting of articles using the Api
class ArticleRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # I want to override through a function the manual input
    #  of a user or author through the API
    # naming convention as_per below (get_queryset) function

    """def perform_create(self, serializer):
        serializer.save(
            author = self.request.user.author
        )"""

    def get_queryset(self):
        author = self.request.user.author
        return Articles.objects.filter(author=author)
