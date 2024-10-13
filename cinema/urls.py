from django.contrib import admin
from django.urls import path

from cinema_app.views.home_view import HomeView
from cinema_app.views.movie_view import MovieView
from cinema_app.views.purchase_ticket_view import PurchaseTicketView

from django.conf.urls.static import static
from django.conf import settings

from cinema_app.views.ticket_success_view import TicketSuccessView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('movie/<int:id>/', MovieView.as_view(), name='movie'),
    path('purchase_ticket/<int:movie_id>', PurchaseTicketView.as_view(), name='purchase_ticket'),
    path('purchase_success',TicketSuccessView.as_view(), name='ticket_success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
