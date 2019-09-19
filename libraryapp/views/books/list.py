#import from python first, Django second, and your own modules thirs
import sqlite3
from ..connection import Connection
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect
from libraryapp.models import Book
from libraryapp.models import model_factory

@login_required
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
        #context is the data to be used in the template
        context = {
            'all_books': all_books
        }
        #In DJANGO you have to manually wire up URLs
        return render(request, template, context)
#Handle the case of a reque
    elif request.method == 'POST':
        #Get some form data
        form_data = request.POST


        #make connection to DB
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO libraryapp_book
            (
                title, author, isbn,
                year_published, location_id, librarian_id
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            #This is a second argument--which is a tuple of the data
            (form_data['title'], form_data['author'],
                form_data['isbn'], form_data['year_published'],
                request.user.librarian.id, form_data["location"]))
        # values as ? prevent hackers from passing SQL injection attacks in

        #After it postts, send them to the booklist
        return redirect(reverse('libraryapp:books'))