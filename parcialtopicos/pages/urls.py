from django.urls import path
from .views import HomePageView, AboutPageView, RegisterFlightView, ProductListFlightsView, FlightStatsView

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path("", AboutPageView.as_view(), name='about'),
    path("", RegisterFlightView.as_view(), name='register'),
    path("", ProductListFlightsView.as_view(), name='list'),
    path("", FlightStatsView.as_view(), name='stats'),
]


