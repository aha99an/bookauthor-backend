from django.contrib import admin
from .models import Author
from django.contrib.auth.admin import UserAdmin


class AuthorUserAdmin(UserAdmin):
    model = Author

admin.site.register(Author, AuthorUserAdmin)


