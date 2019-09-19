import sqlite3
from django.shortcuts import render
from libraryapp.models import Book
from libraryapp.models import model_factory
from ..connection import Connection


def book_list(request):
    # Always have to specify request method for a view
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            #this .row special class puts column headers in place of row indexes...much easier to write code
            conn.row_factory = model_factory(Book)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                b.id,
                b.title,
                b.isbn,
                b.author,
                b.year_published,
                b.librarian_id,
                b.location_id
            from libraryapp_book b
            """)


            all_books = db_cursor.fetchall()
# import book model, create an instance of book and set the book properties to the colums that come back in the dataset.
            # for row in dataset:
            #     book = Book()
            #     book.id = row['id']
            #     book.title = row['title']
            #     book.isbn = row['isbn']
            #     book.author = row['author']
            #     book.year_published = row['year_published']
            #     book.librarian_id = row['librarian_id']
            #     book.location_id = row['location_id']
            #     #append all instances of books to list
            #     all_books.append(book)
        #convert to HTML
        #
        template = 'books/list.html'
        context = {
            'all_books': all_books
        }
        #In DJANGO you have to manually wire up URLs
        return render(request, template, context)