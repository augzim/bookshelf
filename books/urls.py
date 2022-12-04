from django.urls import path

from .models import Book
from .views import (
        AuthorDetailView, AuthorListView,
        BookDetailView, BookListView,
        GenreDetailView, GenreListView,
    )


urlpatterns = [
    path('genres/<int:pk>', GenreDetailView.as_view(), name='genre_detail'),
    path('genres/', GenreListView.as_view(), name='genre_list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('', BookListView.as_view(), name='book_list'),
]
