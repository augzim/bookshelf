from django.contrib import admin
from .models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'quantity', 'is_available']


admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
admin.site.register(Review)
