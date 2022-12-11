from django.urls import path

from .views import (
    AuthorDetailView, AuthorListView,
    BookDetailView, BookListView,
    GenreDetailView, GenreListView,
    ReviewCreateView, ReviewDeleteView, ReviewUpdateView,
)


urlpatterns = [
    path('genres/<slug:genre_slug>', GenreDetailView.as_view(), name='genre_detail'),
    path('genres/', GenreListView.as_view(), name='genre_list'),
    path('authors/<slug:author_slug>/', AuthorDetailView.as_view(), name='author_detail'),
    path('authors/', AuthorListView.as_view(), name='author_list'),

    path(
        '<slug:book_slug>/reviews/create/',
        ReviewCreateView.as_view(),
        name='review_create'
    ),

    path(
        '<slug:book_slug>/reviews/<int:review_pk>/delete/',
        ReviewDeleteView.as_view(),
        name='review_delete'
    ),

    path(
        '<slug:book_slug>/reviews/<int:review_pk>/edit/',
        ReviewUpdateView.as_view(),
        name='review_edit'
    ),

    path('<slug:book_slug>/', BookDetailView.as_view(), name='book_detail'),
    path('', BookListView.as_view(), name='book_list'),
]
