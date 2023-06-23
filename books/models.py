from django.db import models
from users.models import Author

class Book(models.Model):
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(unique=False, max_length=255)
    publish_date = models.DateField( null=True, blank=True)    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.id