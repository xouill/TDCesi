from django.db import models

# Create your models here.


class Groupe(models.Model):

    photoDeGroupe = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return "{} {}".format(
            self.photoDeGroupe if self.photoDeGroupe is not None else '???',
            self.nom if self.nom is not None else '???',
            self.genre if self.genre is not None else '???',
            self.description if self.description is not None else '???'
        )

class Concert(models.Model):
    intitule = models.CharField(max_length=200)
    groupe = models.ForeignKey(Groupe,
                               on_delete=models.CASCADE,
                               default="none",
                               related_name='groupe')
    lieux = models.CharField(max_length=200)
    placeMax = models.IntegerField()


class PlaceVendu(models.Model):

    concert = models.ForeignKey(Concert,
                                on_delete=models.DO_NOTHING,
                                default="none",
                                related_name='concert'
                                )
    adresseMail = models.CharField(max_length=200)
    place = models.IntegerField()
