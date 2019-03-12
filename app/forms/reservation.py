from django.forms import models

from app.models import PlaceVendu, TypePlace


class ConcertReservationForm(models.ModelForm):

    class Meta:
        model = PlaceVendu
        fields = ('adresse_mail', 'concert', 'type_place', 'nombre_place')

    def clean_adresse_mail(self):  # renvoie la valeur et née toi le champs titre
        adresse_mail = self.cleaned_data['adresse_mail']
        if adresse_mail != '':
            return adresse_mail
        self.add_error('adresse_mail', 'le titre ne doit pas être vide ')
        return None

