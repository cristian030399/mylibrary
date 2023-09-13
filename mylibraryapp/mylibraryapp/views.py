from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from users.models import User

def index(request):
    # Create user and save to the database
    # user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

    # # Update fields and then save again
    # user.first_name = 'Tyrone'
    # user.last_name = 'Citizen'
    # user.save()
    # if(not request.user.is_authenticated):
    #     return HttpResponseRedirect(reverse('auth:login'))
    # print(request.user.is_authenticated)
    return HttpResponse("Hola")