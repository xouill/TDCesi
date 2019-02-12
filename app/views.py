from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from app.models import Groupe


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        result = super(IndexView, self).get_context_data(**kwargs)
        result['groupes'] = Groupe
        return result
