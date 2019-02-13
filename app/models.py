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
    groupe = models.ForeignKey(Groupe,
                               on_delete=models.CASCADE,
                               default="none",
                               related_name='groupe')
    lieux = models.CharField(max_length=200)
    prix = models.IntegerField()
    placeMax = models.IntegerField()

    def __str__(self):
        return self.intitule if self.intitule is not None else "erreur"


class TypePlace(models.Model):
    place = models.CharField(max_length=200)
    prixPlace = models.IntegerField(default=0)

    def __str__(self):
        return self.place if self.place is not None else "erreur"


class PlaceVendu(models.Model):
    concert = models.ForeignKey(Concert,
                                on_delete=models.DO_NOTHING,
                                default="none",
                                related_name='concert'
                                )
    adresseMail = models.CharField(max_length=200)
    place = models.ForeignKey(TypePlace,
                               on_delete=models.DO_NOTHING,
                               default="none",
                               related_name='TypePlace')

    def __str__(self):
        return self.concert if self.concert is not None else "erreur"
