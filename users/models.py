from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser



class Author(AbstractUser):
    username = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return str(self.id)