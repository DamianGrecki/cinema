from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.http import HttpResponse
from cinema_app.services.movie_service import MovieService
from cinema_app.services.seat_service import SeatService
from cinema_app.services.ticket_service import TicketService


class PurchaseTicketView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.movie_service = MovieService()
        self.seat_service = SeatService()
        self.ticket_service = TicketService()

    def get(self, request, movie_id):
        movie = self.movie_service.get_movie_by_id(movie_id)
        available_seats = self.seat_service.get_available_seats(movie)
        return render(request, 'purchase_ticket.html', {
            'movie': movie,
            'seating_chart': self.seat_service.get_seating_chart(available_seats)
        })

    def post(self, request, movie_id):
        movie = MovieService().get_movie_by_id(movie_id)
        selected_seats = request.POST.getlist('seats')
        if not selected_seats:
            return HttpResponse("Nie wybrano miejsc.")
        self.ticket_service.purchase_ticket(movie, selected_seats)
        return redirect('ticket_success')
