from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.views import View
from django import forms
from .models import Flight

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Flight manage",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Victor",
        })
        return context
    
class RegisterFlightView(View):
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context.update({
                "title": "About us - Online Store",
                "subtitle": "About us",
                "description": "This is an about page ...",
                "author": "Developed by: Victor",
            })
            return context


class ListFlightsView(ListView):
    template_name = 'pages/list.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Flights"
        viewData["subtitle"] = "List of Flisghts"
        viewData["products"] = Flight.objects.all()
        return render(request, self.template_name, viewData)
    
class FlightStatsView(TemplateView):
    template_name = 'pages/stats.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Flight stats",
            "subtitle": "Flight stats",
            "description": "This is a flight stats page",
            "author": "Developed by: Victor",
        })
        return context           


