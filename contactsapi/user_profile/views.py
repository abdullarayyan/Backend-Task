from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import UserProfile
from .serializers import user_profileSerializer
from rest_framework import permissions


class UserList(ListCreateAPIView):

    serializer_class = user_profileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return UserProfile.objects.filter(owner=self.request.user)


class UserListDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = user_profileSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return UserProfile.objects.filter(owner=self.request.user)