from django.views import View
from django.shortcuts import render, get_object_or_404
from cinema_app.models.movies import Movies

class MovieView(View):
    def get(self, request, id):
        movie = get_object_or_404(Movies, id=id)
        return render(request, 'movie.html', {'movie': movie})