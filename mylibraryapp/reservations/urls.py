from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('', views.IndexViews.as_view(), name='reservations'),
    path('my/', views.MyReservationsView.as_view(), name='my'),
    path('<int:reservation_id>', views.ReservationViews.as_view(), name='reservation'),
    path('<int:reservation_id>/return', views.returnBook, name='return'),
]