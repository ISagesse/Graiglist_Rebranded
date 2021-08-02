from django.shortcuts import render, redirect
from .models import Search
from bs4 import BeautifulSoup
import requests

# Create your views here.
def index(request):
    return render(request, "base.html")

def result(request):
    user_search = request.session['my_search']
    context = {
        'result': user_search
    }
    return render(request, "new_search.html", context)

def new_search(request):
    user_search = request.POST['search']
    request.session['my_search'] = user_search
    return redirect('/result')