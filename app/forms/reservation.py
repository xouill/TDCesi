from django.forms import models

from app.models import PlaceVendu

class ConcertReservationForm(models.ModelForm):

    class Meta:
        model = PlaceVendu
        fields = ('adresseMail', 'concert', 'place')

    def clean_titre(self):  # renvoi la valoir et nétoi le champs titre
        titre = self.cleaned_data['adresseMail']
        if titre != '':
            return titre
        self.add_error('adresseMail', 'le titre ne doit pas être vide ')
        return None

    # def clean(self): # clean général ( utiliser dans le cas de mdp
