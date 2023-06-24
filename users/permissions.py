from rest_framework.permissions import BasePermission
from books.models import Book

class IsOwnBook(BasePermission):
    """
    Allows users if they are Author for this book
    """

    def has_object_permission(self, request, view, obj):
        if obj.author.id == request.user.id:
            return True
        return False




class IsOwnPage(BasePermission):
    """
    Allows users if they are Author for this book
    """
    def has_permission(self, request, view):
        book_id = view.kwargs.get('book_id')
        book = Book.objects.filter(id=book_id, author=request.user).exists()
        return book
    
    def has_object_permission(self, request, view, obj):
        if obj.book.author.id == request.user.id:
            return True
        return False
