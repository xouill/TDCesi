from django.contrib import admin
from app.models import Groupe
from app.models import Concert
from app.models import PlaceVendu
# Register your models here.

admin.site.register(Groupe)
admin.site.register(Concert)
admin.site.register(PlaceVendu)
