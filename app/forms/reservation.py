from django.forms import models
from django import forms

from app.models import PlaceVendu


class ConcertReservationForm(models.ModelForm):

    class Meta:
        model = PlaceVendu
        fields = ('adresseMail', 'concert', 'place', 'nombrePlace')

    def clean_adresseMail(self):  # renvoi la valeur et née toi le champs titre
        adresseMail = self.cleaned_data['adresseMail']
        if adresseMail != '':
            return adresseMail
        self.add_error('adresseMail', 'le titre ne doit pas être vide ')
        return None


