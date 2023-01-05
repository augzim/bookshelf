from django.urls import path

from .views import (
    AuthorDetailAPIView, AuthorListAPIView,
    BookDetailAPIView, BookListAPIView,
    GenreDetailAPIView, GenreListAPIView,
    # ReviewAPIView,
    # ReviewCreateAPIView, ReviewDeleteAPIView, ReviewListAPIView, ReviewUpdateAPIView,
)


urlpatterns = [
    path('authors/<slug:author_slug>/', AuthorDetailAPIView.as_view()),
    path('authors/', AuthorListAPIView.as_view()),

    # reviews
    # path('books/<slug:book_slug>/reviews/<int:review_pk>/delete/', ReviewDeleteAPIView.as_view()),
    # path('books/<slug:book_slug>/reviews/<int:review_pk>/edit/', ReviewUpdateAPIView.as_view()),
    # path('books/<slug:book_slug>/reviews/create/', ReviewAPIView.as_view()),
    # path('books/<slug:book_slug>/reviews/create/', ReviewCreateAPIView.as_view()),
    # path('books/<slug:book_slug>/reviews/', ReviewAPIView.as_view()),

    path('books/<slug:book_slug>/', BookDetailAPIView.as_view()),
    path('books/', BookListAPIView.as_view()),

    path('genres/<slug:genre_slug>/', GenreDetailAPIView.as_view()),
    path('genres/', GenreListAPIView.as_view()),
]