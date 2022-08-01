from django.contrib import admin
from .models import Book, User, Note, Status

admin.site.register(Book)
admin.site.register(User)
admin.site.register(Note)
admin.site.register(Status)
