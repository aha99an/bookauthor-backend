from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwnBook


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated,IsOwnBook]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated,IsOwnBook]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        data = request.data
        data["author"] = request.user.pk
        return super().create(request, *args, **kwargs)
