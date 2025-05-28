from django.shortcuts import render, get_object_or_404
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def book_history(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    histories = book.borrow_history.all()     
    return render(request, 'library/book_history.html', {
        'book': book,
        'histories': histories,
    })