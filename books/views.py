# from typing_extensions import Self
from django.shortcuts import render
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, renderers, filters
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Book, User, Status, Note
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly, IsOwner, IsPublic
from .serializers import BookSerializer, NoteSerializer, StatusSerializer


class BookList(generics.ListCreateAPIView):
    # allows list and creation of books

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # allows creation of book if authenticated

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'author']
    filterset_fields = ['featured']
    # need to set featured field as read-only


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAdminOrReadOnly,)


class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['book']
    filterset_fields = ['owner']
    permission_classes = (IsPublic, IsOwner,)
    # still need to figure out how to show all public notes
    # and only own private notes

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        # when a note instance is saved,
        # the owner is the user that made the request


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


class StatusList(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['book']
    filterset_fields = ['status_choices']
    permission_classes = (IsOwner)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        # when a note instance is saved,
        # the owner is the user that made the request


class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = (IsOwner)
