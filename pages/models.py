from django.db import models
from books.models import Book

class Page(models.Model):
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    page_no=models.IntegerField()
    content= models.CharField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.id