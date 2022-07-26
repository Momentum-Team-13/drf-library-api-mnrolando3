# DRF Library API

Create a new API-only application that lets users keep track of books, including important information like title, author, publication date, a genre, and a field that marks it as "featured". Books should be unique by title and author (that is, you can't have two books with the same title _and_ author; two books with the same title is fine as long as the authors are different).

Users should be able to search for a book by title or author.

Anyone can add a new book as long as the same book is not already in the library. Only admin users can update book details (like whether it is "featured") and delete books.
- So is this just a database collection of ANY book or a collection of books read or owned by a particular user? ANY book

You'll also need a book tracking model so that users can mark a book as "want to read", "reading", or "read/done"; this status can also be updated. The tracking model should have a foreign key to a book and to a user.
- View/read/get does not require login; marking/patching/updating does require login
- Tracking model ~ tracker in HabitTracker project

Optionally users can take notes on books. These notes have a foreign key relationship with a book and a user, a datetime they are created, a note body, a boolean field marking it as public or private, and an optional page number. Private notes are viewable only by the author. When notes are retrieved, return them by creation time in reverse order.

Users should be able to see a list of all the books they are tracking, or a list by status (for instance, all their "want to read" books). You _could_ consider using [DjangoFilterBackend](https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend) for this.
- books with all tracking objects
- books with specific on tracking objects

You should _not_ make forms or templates for this app, but you will need models, urls, views, and serializers. You should use class-based views and return JSON responses.

Your app should allow users to:

- list all books - DONE
- list all featured books - DONE
- create a book - DONE
- retrieve details about a book - DONE
- search books by author or title - DONE

- see a list of all the books they are tracking and their statuses
    - can see list of all statuses

- see a list of all their books by status (e.g., all the books they have marked as "read") - DONE
- mark a book as want to read, reading, or read - DONE
- update the want to read/reading/read status of a book - DONE

- retrieve all their own private notes for a book
- retrieve all public notes for a book

- create a note for a book - DONE
- edit their own notes - DONE

Admin users can:

- update a book (including marking/unmarking it as featured) - DONE
- delete a book (this should not delete notes about a book)
    - no delete=models.CASCADE on tracking model FK

You'll need to use Insomnia (or some other tool for making requests) to test your API as you are building it.

image.png

