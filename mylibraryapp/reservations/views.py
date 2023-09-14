from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import createForm
from books.models import Book
from .models import Reservation
from django.views import generic

# Create your views here.

class IndexViews(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = createForm(request.POST)
        if(not form.is_valid()):
            messages.error(request, 'Select valid Date')
            return HttpResponseRedirect(reverse('books:detail', args=(book.id,)))
        
        book = get_object_or_404(Book, pk=form.cleaned_data['book'])
        if(book.isRented):
            messages.error(request, 'test')
            return HttpResponseRedirect(reverse('books:detail', args=(book.id,)))
        newReservation = Reservation(date_finish=form.cleaned_data['date_finish'], user=request.user, book=book)
        book.isRented = True
        newReservation.save()
        book.save()
        return HttpResponseRedirect(reverse('reservations:my'))
        # return HttpResponseRedirect(reverse('reservations:reservation', args=(newReservation.id,)))

class ReservationViews(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
              
        print(kwargs)
        return HttpResponse('Entró acá')

class MyReservationsView(LoginRequiredMixin, generic.ListView):
    template_name= 'reservations/my.html'
    context_object_name = 'reservations'

    def get_queryset(self) -> QuerySet[Any]:
        user = self.request.user
        return Reservation.objects.filter(user = user.id)

@login_required(())
def returnBook(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    reservation.was_returned = True
    book = reservation.book
    book.isRented = False
    reservation.save()
    book.save()
    return HttpResponseRedirect(reverse('reservations:my'))