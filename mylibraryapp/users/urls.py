from django.urls import path, include 
from . import views

app_name = 'auth'
urlpatterns = [
    path('create/', views.create_user, name='create'),
    path('signup/', views.show_signup_form, name='signup'),
    path('', include('django.contrib.auth.urls')),
]