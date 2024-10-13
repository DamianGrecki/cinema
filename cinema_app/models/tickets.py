from django.db import models
from cinema_app.models.movies import Movies
from cinema_app.models.seats import Seats


class Tickets(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    seat = models.OneToOneField(Seats, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
