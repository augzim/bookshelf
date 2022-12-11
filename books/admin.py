from django.contrib import admin
from .models import *


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'quantity', 'is_available']
    prepopulated_fields = {'slug': ('title', )}


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Review)
