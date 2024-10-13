from django.shortcuts import get_object_or_404
from cinema_app.models.movies import Movies


class MovieService:
    def get_movie_by_id(self, movie_id: int):
        return get_object_or_404(Movies, pk=movie_id)

    def getLatestAddMovies(self, limit: int):
        return Movies.objects.order_by('-created_at')[:limit]