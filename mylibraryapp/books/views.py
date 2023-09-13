from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'books/index.html'
    context_object_name = 'book_list'

    def get_queryset(self) -> QuerySet[Any]:
        return Book.objects.filter(isRented=False)
    
class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Book
    template_name = 'books/detail.html'

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     return super().get_context_data(**kwargs)
