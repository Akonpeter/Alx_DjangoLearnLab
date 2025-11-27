from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Book
from rest_framework import generics
from .serializers import BookSerializer


class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"


class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"


class BookCreateView(CreateView):
    model = Book
    fields = ["title", "author", "publication_year"]
    template_name = "books/book_form.html"
    success_url = reverse_lazy("book_list")


class BookUpdateView(UpdateView):
    model = Book
    fields = ["title", "author", "publication_year"]
    template_name = "books/book_form.html"
    success_url = reverse_lazy("book_list")


class BookDeleteView(DeleteView):
    model = Book
    template_name = "books/book_confirm_delete.html"
    success_url = reverse_lazy("book_list")


from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# List all books + Create new book
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Retrieve one book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Update a book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    filterset_fields = ["author"]
    search_fields = ["title", "author"]
