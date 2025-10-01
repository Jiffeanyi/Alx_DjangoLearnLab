from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library

def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})
