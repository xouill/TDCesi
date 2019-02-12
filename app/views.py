from django.shortcuts import render

# Create your views here.
from app.models import Groupe
from django.views.generic import TemplateView, DetailView
from app.models import Concert


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        result = super(IndexView, self).get_context_data(**kwargs)
        result['groupes'] = Groupe.objects
        return result


class ConcertDetailView(DetailView):

    template_name = 'detail.html'
    model = Concert
