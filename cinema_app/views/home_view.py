from django.shortcuts import render
from django.views import View

from cinema_app.services.movie_service import MovieService


class HomeView(View):
    def get(self, request):
        latest_movies = MovieService().getLatestAddMovies(6)
        context = {
            'text': 'Witaj na stronie głównej!',
            'latest_movies': latest_movies
        }
        return render(request, 'home.html', context)
