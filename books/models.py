# from lib2to3.pgen2.pgen import generate_grammar
# from multiprocessing import AuthenticationError
# from turtle import title
# from typing_extensions import Self
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.db.models.constraints import UniqueConstraint


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.username} {self.email}'


class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=250)
    publication_date = models.DateField()
    genre = models.CharField(max_length=100)
    featured = models.BooleanField()

    def __str__(self):
        return f'{self.title} {self.author}'

    # need more information about what constraints are and how this works
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'],
                                    name='unique_book')
        ]


class Status(models.Model):
    READ = 'RD'
    READING = 'RDING'
    WANT_TO_READ = 'WTR'
    STATUS_CHOICES = [
        (READ, 'Read'),
        (READING, 'Reading'),
        (WANT_TO_READ, 'Want to read'),
    ]
    status_choices = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=WANT_TO_READ,
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='user_statuses')
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='book_statuses')

    def __str__(self):
        return f'{self.status_choices}'


class Note(models.Model):
    note = models.TextField()
    page_number = models.CharField(max_length=10, null=True, blank=True)
    public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='user_notes')
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='book_notes')

    def __str__(self):
        return f'{self.note}'
