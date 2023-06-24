from django.shortcuts import render
from rest_framework import viewsets
from .models import Page
from .serializers import PageSerializer

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def get_queryset(self):
        queryset = Page.objects.filter(book_id=self.kwargs['book_id'])
        return queryset
    
   