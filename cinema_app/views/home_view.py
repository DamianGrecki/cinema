# cinema_app/home_view.py
from cinema_app.models.movies import Movies
from django.shortcuts import render

def home(request):
    latest_movies = Movies.objects.order_by('-created_at')[:6]
    context = {
        'text': 'Witaj na stronie głównej!',
        'latest_movies': latest_movies
    }
    return render(request, 'home.html', context)
