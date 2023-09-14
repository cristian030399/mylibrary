from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from users.models import User
from books.models import Book
from reservations.models import Reservation
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponseRedirect(reverse('books:index'))

@login_required(())
def showAdmin(request):
    if(not request.user.is_superuser):
        return render(request, 'error/notPermissionPage.html')
    books = Book.objects.all()
    reservations = Reservation.objects.all()
    return render(request, 'admin/index.html', {
        'books': books,
        'reservations': reservations
    })