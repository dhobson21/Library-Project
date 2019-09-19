import sqlite3
from django.shortcuts import render
from libraryapp.models import Library
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect
from libraryapp.models import model_factory
from ..connection import Connection

@login_required
def library_list(request):
    if request.method == "GET":
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Library)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                l.id,
                l.title,
                l.address
    from libraryapp_library l;
            """)

            all_libraries = db_cursor.fetchall()

        template_name = 'libraries/list.html'
        return render(request, template_name, {'all_libraries': all_libraries})

    elif request.method == "POST":
        form_data = request.POST


        #make connection to DB
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO libraryapp_library
            (
                title, address
            )
            VALUES (?, ?)
            """,
            #This is a second argument--which is a tuple of the data
            (form_data['name'], form_data['address']))
        # values as ? prevent hackers from passing SQL injection attacks in

        #After it postts, send them to the librarylist
        return redirect(reverse('libraryapp:libraries'))