from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout

#reverse is an imported method that goes into URLs.py and reverse looks up the url based on the name you send in "home"


# 'libraryapp:home' is calling the libraryapp urls.py file (namespacing) and the name="home" which will return the url attached

def logout_user(request):
    logout(request)
    return redirect(reverse('libraryapp:home'))