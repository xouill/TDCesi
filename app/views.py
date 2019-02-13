from django.http import request
from django.shortcuts import render

# Create your views here.
from app.models import Groupe, Concert, PlaceVendu
from django.views.generic import TemplateView, DetailView, ListView, FormView

from app.forms.reservation import ConcertReservationForm
from django.urls import reverse_lazy
from django.core.mail import send_mail


class IndexView(TemplateView):
    template_name = 'index.html'


class ConcertDetailView(DetailView):
    template_name = 'detail.html'
    model = Concert


class ConcertListView(ListView):
    template_name = 'list_view.html'
    model = Concert


class ConcertReservationFormView(FormView):
    form_class = ConcertReservationForm
    template_name = 'reservation.html'
    success_url = reverse_lazy('reservation')  # redirection quand réussi

    def get_initial(self):
        initial = super(ConcertReservationFormView, self).get_initial()
        initial['adresseMail'] = ''
        return initial

    def form_valid(self, form):
        send_mail('Hello',
                  'LOL',
                  '',
                  request.POST.get('from_email', ''),
                  fail_silently=False)
        # si le formulaire est valide on arrive ici
        return super(ConcertReservationFormView, self).form_valid(form)
        # faire la liaison avec la bdd

