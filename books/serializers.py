from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    # # set owner var as a readonly field
    # # source populates field based on specified attribute owner's username

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'publication_date',
            'genre',
            'featured',
            # 'owner',
        ]
# creates class that uses Book model and outputs the table fields