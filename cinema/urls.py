# myproject/urls.py
from django.contrib import admin
from django.urls import path
from cinema_app.views.home_view import home
from cinema_app.views.movie_view import MovieView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('movie/<int:id>/', MovieView.as_view(), name='movie'),
]
