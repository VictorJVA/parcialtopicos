from django.urls import path
from .views import HomePageView, AboutPageView, RegisterFlightView, ListFlightsView, FlightStatsView, ProductShowView

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path("register/", RegisterFlightView.as_view(), name='register'),
    path("list/", ListFlightsView.as_view(), name='list'),
    path("product/<int:id>", ProductShowView.as_view(), name='show'),
    path("stats/", FlightStatsView.as_view(), name='stats'),
]