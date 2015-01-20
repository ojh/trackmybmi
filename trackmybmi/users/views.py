from django.shortcuts import render

from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """This endpoint presents the users in the system."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
