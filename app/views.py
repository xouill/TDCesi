from django.shortcuts import render

# Create your views here.
from app.models import Groupe
from django.views.generic import TemplateView, DetailView, ListView
from app.models import Concert


class IndexView(TemplateView):
    template_name = 'index.html'


class ConcertDetailView(DetailView):
    template_name = 'detail.html'
    model = Concert


class ConcertListView(ListView):
    template_name = 'list_view.html'
    model = Groupe
