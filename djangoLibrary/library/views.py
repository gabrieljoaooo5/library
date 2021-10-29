from django.forms import ModelForm
from .models import *
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'publisher', 'isbn', 'pagesNumber', 'title', 'publicationYear', 'publisherEmail']

def book_list(request, template_name='book_list.html'):
    book = Book.objects.all()
    books = {'list': book}
    return render(request, template_name, books)

def book_new(request, template_name='book_form.html'):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, template_name, {'form': form})


def book_edit(request, pk, template_name='book_form.html'):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, template_name, {'form': form})

def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'book_delete.html', {'book': Book})
