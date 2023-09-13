from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from users.models import User

def index(request):
    return HttpResponseRedirect(reverse('books:index'))