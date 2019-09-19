from django.conf.urls import url, include
from .views import *


# namespacing this file so that you can tell reverse to lookup 'libraryapp:books to return books url
app_name = "libraryapp"

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^books$', book_list, name='books'),
    url(r'^librarians$', list_librarians, name='librarians'),
    url(r'^libraries$', library_list, name='libraries'),
    #The below lets application use built in login screen
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^book/form$', book_form, name='book_form'),
    url(r'^library/form$', library_form, name='library_form'),
]