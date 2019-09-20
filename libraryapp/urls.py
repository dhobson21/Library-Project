from django.conf.urls import url, include
from django.urls import path
from .views import *


# namespacing this file so that you can tell reverse to lookup 'libraryapp:books to return books url
app_name = "libraryapp"

urlpatterns = [
    #url v path
    #url has to take a regular expression
    #path can take the string of the path
    url(r'^$', home, name='home'),
    path('books/', book_list, name='books'),
    path('book/form', book_form, name='book_form'),
    path('books/<int:book_id>/', book_details, name='book'),
    path('libraries/', library_list, name='libraries'),
    path('library/form', library_form, name='library_form'),
    path('libraries/<int:library_id>/', library_details, name='library'),
    path('librarians/', list_librarians, name='librarians'),
    path('librarians/<int:librarian_id>/', librarian_details, name='librarian'),
    #The below lets application use built in login screen
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/$', logout_user, name='logout'),
    url(r'^books/(?P<book_id>[0-9]+)/form$', book_edit_form, name='book_edit_form'),
]