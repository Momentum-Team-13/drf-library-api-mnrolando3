from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Book, User, Status, Note
from .permissions import IsAdminOrReadOnly
from .serializers import BookSerializer, NoteSerializer


class BookList(generics.ListCreateAPIView):
    # allows creation of list of all Book objects
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # need to set featured field as read-only


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAdminOrReadOnly,)


class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    # permission_classes = (IsPublic, IsOwner,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        # when a note instance is saved,
        # the owner is the user that made the request