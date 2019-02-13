from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from app import views
from app.views import IndexView, ConcertDetailView, ConcertReservationFormView, ConcertListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    url(r'detail/(?P<pk>[0-9]+)', ConcertDetailView.as_view(template_name='detail.html'), name='detail'),
    url(r'reservation/(?P<pk>[0-9]+)', ConcertReservationFormView.as_view(template_name='reservation.html'), name='reservation'),
    url('list', ConcertListView.as_view(template_name='list_view.html'), name='list'),
]
