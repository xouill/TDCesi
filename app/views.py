import re

from django.contrib import messages
from django.http import request

# Create your views here.
from app.models import Groupe, Concert, TypePlace, PlaceVendu
from django.views.generic import TemplateView, DetailView, ListView, FormView

from app.forms.reservation import ConcertReservationForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from urllib import request
from django.http import request

class IndexView(TemplateView):
    template_name = 'index.html'

class ConcertDetailView(DetailView):
    template_name = 'detail.html'
    model = Concert

    def get_context_data(self, **kwargs):
        result = super(ConcertDetailView, self).get_context_data(**kwargs)
        result['type_place'] = TypePlace.objects.filter(concert=self.object)  # moddifier pour récupérer la pk dans l'url !!

        return result

class ConcertListView(ListView):
    template_name = 'list_view.html'
    model = Concert

class ConcertReservationFormView(FormView):
    form_class = ConcertReservationForm
    template_name = 'reservation.html'

    def __init__(self, **kwargs):
        self.email = None
        self.place = None
        self.concert = None
        super(ConcertReservationFormView, self).__init__(**kwargs)

    def get_initial(self, **kwargs):
        initial = super(ConcertReservationFormView, self).get_initial()
        initial['adresseMail'] = ''
        initial['concert'] = Concert.objects.get(pk=self.kwargs['pk'])  # a faire pour rendre dymanique par rapport a la pk dans l'url
        # initial['place'] = TypePlace.objects.all().filter(Concert_id=self.kwargs['pk'])
        return initial

    def form_valid(self, form):
        # https://stackoverflow.com/questions/201323/how-to-validate-an-email-address-using-a-regular-expression
        regex = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-" \
                r"\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-" \
                r"9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.)" \
                r"{3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-" \
                r"\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        self.email = form.cleaned_data.get('adresseMail', None)
        if self.email is None:
            form.add_error('adresseMail','Email vide')
            return super(ConcertReservationFormView, self).form_invalid(form)

        self.place = form.cleaned_data.get('place', None)
        self.concert = form.cleaned_data.get('concert')

        # FAIRE LE TYPE DE PLACE
        if not re.match(regex, self.email):
            form.add_error('adresseMail','Adresse Email invalide')
            return super(ConcertReservationFormView, self).form_invalid(form)

        # Envoi de l'email
        send_mail('Réservation Concert',  #Subject
                  'Vous avez réservé ' + self.place+' places pour le concert :' + self.concert.intitule,  #Message
                  '',  #emailFrom
                  #['noreply.cesi.concert@gmail.com'], #emailTo
                  [self.email, ],  # emailTo
                  fail_silently=False)

        # si le formulaire est valide on arrive ici
        concert = Concert.objects.get(pk=form.cleaned_data['concert'])
        place = TypePlace.objects.get(pk=form.cleaned_data['place'])
        PlaceVendu.objects.create(concert=concert,
                                  adresseMail=form.cleaned_data['adresseMail'],
                                  place=place,
                                  nombrePlace=form.cleaned_data['nombrePlace'])
        PlaceVendu.save()
        return super(ConcertReservationFormView, self).form_valid(form)
        # faire la liaison avec la bdd

    def get_success_url(self):
        #Message à utilisation unique
        messages.success(self.request, 'Réservation effectuée pour {}'.format(self.email))
        messages.success(self.request, 'Nombre de places {}'.format(self.place))

        return reverse_lazy('success', kwargs={"pk": self.kwargs['pk']})