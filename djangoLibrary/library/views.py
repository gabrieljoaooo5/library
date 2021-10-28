from django.forms import ModelForm
from .models import *
from django.shortcuts import render

# Create your views here.

class BookForm(ModelForm):
    model = Book
    fields = ['author', 'publisher', 'isbn', 'pagesNumber', 'title', 'publicationYear', 'publisherEmail']

def book_list(request, template_name='book_list.html'):
    book = Book.objects.all()
    books = {'list': book}
    return render(request, template_name, books)
