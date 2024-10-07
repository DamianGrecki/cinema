# myproject/urls.py
from django.contrib import admin
from django.urls import path
from cinema_app.views.home_view import home
from cinema_app.views.movie_view import MovieView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('movie/<int:id>/', MovieView.as_view(), name='movie'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
