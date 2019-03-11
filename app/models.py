from django.db import models


# Create your models here.


class Groupe(models.Model):
    photoDeGroupe = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.nom if self.nom is not None else "erreur"


class Concert(models.Model):
    intitule = models.CharField(max_length=200)
    lieux = models.CharField(max_length=200)
    placeMax = models.IntegerField()
    date = models.DateField(default="2019-02-13")
    groupe = models.ForeignKey(Groupe,
                               on_delete=models.DO_NOTHING,
                               default=1,
                               null=True,
                               related_name='Groupe'
                               )

    def __str__(self):
        return self.intitule if self.intitule is not None else "erreur"


class TypePlace(models.Model):
    place = models.CharField(max_length=200)
    prixPlace = models.IntegerField(default=0)
    concert = models.ForeignKey(Concert,
                                on_delete=models.DO_NOTHING,
                                default=-1,
                                null=True,
                                related_name='concertTypePlace'
                                )

    def __str__(self):
        return self.place if self.place is not None else "erreur"


class PlaceVendu(models.Model):
    concert = models.ForeignKey(Concert,
                                on_delete=models.DO_NOTHING,
                                default=-1,
                                null=True,
                                related_name='concertPlaceVendu'
                                )
    adresseMail = models.EmailField()
    nombrePlace = models.IntegerField(default=1)
    place = models.CharField(max_length=200)

    def __str__(self):
        return self.concert.intitule if self.concert.intitule is not None else "erreur"


    #ADD EN BASE
    def save_model(self,request,PlaceVendu,ConcertReservationFormView):