from django.shortcuts import redirect, render
from django.views import View
from cinema_app.services.movie_service import MovieService
from cinema_app.services.seat_service import SeatService
from cinema_app.services.ticket_service import TicketService


class PurchaseTicketView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.movie_service = MovieService()
        self.seat_service = SeatService()
        self.ticket_service = TicketService()

    def get(self, request, movie_id: int):
        movie = self.movie_service.get_movie_by_id(movie_id)
        available_seats = self.seat_service.get_available_seats(movie)
        error_message = request.session.pop('error_message', None)
        return render(request, 'purchase_ticket.html', {
            'movie': movie,
            'seating_chart': self.seat_service.get_seating_chart(available_seats),
            'error_message': error_message
        })

    def post(self, request, movie_id: int):
        movie = MovieService().get_movie_by_id(movie_id)
        selected_seats = request.POST.getlist('seats')
        if not selected_seats:
            message = "Nie wybrano miejsc!"
            return self.handle_error(request, message, movie_id)
        try:
            self.ticket_service.purchase_ticket(movie, selected_seats)
            return redirect('ticket_success')
        except ValueError as e:
            return self.handle_error(request, e, movie_id)

    def handle_error(self, request, error_message: str, movie_id: int):
        request.session['error_message'] = str(error_message)
        return redirect('purchase_ticket', movie_id=movie_id)
