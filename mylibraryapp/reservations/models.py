from django.db import models
from users.models import User
from books.models import Book

class Reservation(models.Model):
    date_start = models.DateTimeField(auto_now=True)
    date_finish = models.DateTimeField()
    observation = models.TextField(default='')
    was_returned = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
