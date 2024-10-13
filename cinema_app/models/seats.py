from django.db import models

from cinema_app.models.movies import Movies


class Seats(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    row = models.CharField(max_length=1)
    number = models.IntegerField()
    objects = models.Manager()

    def __str__(self):
        return f"Row {self.row}, Seat {self.number}"