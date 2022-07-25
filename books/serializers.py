from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Book, Note


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'publication_date',
            'genre',
            'featured',
        ]
# creates class that uses Book model and outputs the table fields


class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # # set owner var as a readonly field
    # # source populates field based on specified attribute owner's username

    class Meta:
        model = Note
        fields = [
            'note',
            'page_number',
            'public',
            'created_at',
            'book',
            'owner',
        ]