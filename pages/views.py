from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Page
from .serializers import PageSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwnPage
from rest_framework.response import Response

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated,IsOwnPage]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated,IsOwnPage]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated,IsOwnPage]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        queryset = Page.objects.filter(book_id=self.kwargs['book_id'])
        return queryset
   
    def create(self, request, *args, **kwargs):
        page_no = request.data.get('page_no')
        book_id = self.kwargs['book_id']

        if Page.objects.filter(book_id=book_id, page_no=page_no).exists():
            return Response(
                {'detail': 'Page number already exists for this book.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        data = request.data
        book_id= self.kwargs['book_id']
        data["book"] = book_id
        return super().update(request, *args, **kwargs)


