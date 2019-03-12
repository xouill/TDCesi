import re

from django.contrib import messages

# Create your views here.
from app.models import Concert, TypePlace, PlaceVendu
from django.views.generic import TemplateView, DetailView, ListView, FormView

from app.forms.reservation import ConcertReservationForm
from django.urls import reverse_lazy
from django.core.mail import send_mail


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
        # Constructeur
        super(ConcertReservationFormView, self).__init__(**kwargs)
        self.adresse_mail = None
        self.concert = None
        self.type_place = None
        self.nombre_place = None
        self.prix = 0

    def get_initial(self, **kwargs):
        initial = super(ConcertReservationFormView, self).get_initial()
        initial['adresse_mail'] = ''
        initial['concert'] = Concert.objects.get(pk=self.kwargs['pk'])
        # initial['type_place'] = TypePlace.objects.all().filter(Concert_id=self.kwargs['pk'])
        return initial

    def form_valid(self, form):
        # prendre ce qui arrive :
        self.adresse_mail = form.cleaned_data.get('adresse_mail')
        self.concert = form.cleaned_data.get('concert')
        self.type_place = form.cleaned_data.get('type_place')
        self.nombre_place = int(form.cleaned_data.get('nombre_place', 0))

        # https://stackoverflow.com/questions/201323/how-to-validate-an-email-address-using-a-regular-expression
        regex = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-" \
                r"\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-" \
                r"9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.)" \
                r"{3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-" \
                r"\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        if self.adresse_mail is None:
            form.add_error('adresse_mail', 'Email vide')
            return super(ConcertReservationFormView, self).form_invalid(form)

            # remplacer par l'objet concerné
        self.concert = Concert.objects.get(intitule=self.concert)
        self.type_place = TypePlace.objects.get(nom=self.type_place)
        self.prix = self.type_place.prix * self.nombre_place

        # FAIRE LE TYPE DE PLACE
        if not re.match(regex, self.adresse_mail):
            form.add_error('adresse_mail', 'Adresse Email invalide')
            return super(ConcertReservationFormView, self).form_invalid(form)

        # Envoi de l'email
        send_mail('Réservation Concert',  # Subject
                  'Vous avez réservé {} place(s) {} pour le concert {}\n'
                  'Prix total : {}'.format(
                      self.nombre_place, self.type_place, self.concert.intitule, self.prix
                  ),  # Message
                  '',  # emailFrom
                  # ['noreply.cesi.concert@gmail.com'], #emailTo
                  [self.adresse_mail, ],  # emailTo
                  fail_silently=False)

        # si le formulaire est valide on arrive ici
        PlaceVendu.objects.create(concert=self.concert,
                                  adresse_mail=self.adresse_mail,
                                  type_place=self.type_place,
                                  nombre_place=self.nombre_place)
        PlaceVendu.save(self.type_place)
        return super(ConcertReservationFormView, self).form_valid(form)
        # faire la liaison avec la bdd

    def get_success_url(self):
        # Message à utilisation unique
        messages.success(self.request, 'Réservation effectuée pour {}'.format(self.adresse_mail))
        messages.success(self.request, 'Nombre de places {}'.format(str(self.nombre_place)))
        messages.success(self.request, 'Type de place {}'.format(str(self.type_place)))
        messages.success(self.request, 'Prix : {}'.format(str(self.prix)))
        return reverse_lazy('success', kwargs={"pk": self.kwargs['pk']})