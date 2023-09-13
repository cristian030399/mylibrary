from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    summary = models.TextField()
    isRented = models.BooleanField(default=False)
