from django.shortcuts import get_object_or_404
from cinema_app.models.seats import Seats
from cinema_app.models.tickets import Tickets
from cinema_app.services.seat_service import SeatService


class TicketService:

    def __init__(self):
        self.seat_service = SeatService()

    def purchase_ticket(self, movie, selected_seats):
        available_seats = self.seat_service.get_available_seats(movie)

        for seat_id in selected_seats:
            seat = get_object_or_404(Seats, id=seat_id)
            if seat not in available_seats:
                raise ValueError(f"Miejsce {seat.number} nie jest dostępne")

            Tickets.objects.create(movie=movie, seat=seat)
