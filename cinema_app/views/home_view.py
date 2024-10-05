# cinema_app/home_view.py
from django.shortcuts import render

def home(request):
    context = {
        'text': 'Witaj na stronie głównej!'
    }
    return render(request, 'home.html', context)
