import pytest
from library.models import Book
from library.services.book_service import get_book_by_id
from library.exceptions import BookNotFound
from library.exceptions import BookHasNoBorrowHistory
from library.services.book_service import get_borrow_history_for_book
from library.models import Book, BorrowHistory
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_get_book_by_id_success():
    book = Book.objects.create(title='Test Book', author='Tester', isbn='1234567890123')
    result = get_book_by_id(book.id)
    assert result == book
    assert result.title == 'Test Book'

@pytest.mark.django_db
def test_get_book_by_id_not_found():
    with pytest.raises(BookNotFound) as exc_info:
        get_book_by_id(9999)

@pytest.mark.django_db
def test_get_borrow_history_for_book_success():
    user = User.objects.create(username='testuser')
    book = Book.objects.create(title='Test Book', author='Tester', isbn='1234567890123')
    BorrowHistory.objects.create(book=book, user=user)

    histories = get_borrow_history_for_book(book)
    assert histories.count() == 1
    assert histories.first().user == user
@pytest.mark.django_db
def test_get_borrow_history_for_book_no_history():
    book = Book.objects.create(title='Empty Book', author='Nobody', isbn='9999999999999')
    with pytest.raises(BookHasNoBorrowHistory) as exc_info:
        get_borrow_history_for_book(book)