from cinema_app.models.movies import Movies
from cinema_app.models.seats import Seats
from cinema_app.models.tickets import Tickets



class SeatService:

    def get_available_seats(self, movie: Movies):
        sold_seats = Tickets.objects.filter(movie=movie).values_list('seat_id', flat=True)
        seats = Seats.objects.filter(movie=movie).order_by('row', 'number')
        return seats.exclude(id__in=sold_seats)


    def get_seating_chart(self, available_seats):
        seating_chart = {}
        for seat in available_seats:
            row = seat.row
            if row not in seating_chart:
                seating_chart[row] = []
            seating_chart[row].append(seat)
        return seating_chart
