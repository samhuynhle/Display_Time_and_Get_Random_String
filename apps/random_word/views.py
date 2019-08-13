from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'counting' in request.session:
        request.session['counting'] += 1
    else: 
        setsession(request)
    return render(request,'random_word/index.html')

def process(request):
    if request.method == "POST":
        request.session['random_string'] = get_random_string(length=14)
        return redirect("/")    

def setsession(request):
    request.session['counting'] = 0
    request.session['random_string'] = get_random_string(length=14)