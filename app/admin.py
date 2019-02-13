from django.contrib import admin
from app.models import Groupe, Concert, PlaceVendu, TypePlace
# Register your models here.

admin.site.register(Groupe)
admin.site.register(Concert)
admin.site.register(PlaceVendu)
admin.site.register(TypePlace)
