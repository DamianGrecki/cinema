from django.shortcuts import render
from django.views import View

class TicketSuccessView(View):
    def get(self, request):
        return render(request, 'ticket_success.html')
