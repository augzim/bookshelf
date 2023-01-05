import datetime

from django.contrib.auth.models import User
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from books.models import Author, Book, Genre
from .serializers import AuthorSerializer, BookSerializer, GenreSerializer, ReviewSerializer


class AuthorDetailAPIView(RetrieveAPIView):
    lookup_field = 'slug'
    lookup_url_kwarg = 'author_slug'
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorListAPIView(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        book = Book.objects.get(slug=kwargs['book_slug'])
        return Response({k: v for k, v in BookSerializer(book).data.items()})


class BookListAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        return Response(BookSerializer(books, many=True).data)


class GenreDetailAPIView(RetrieveAPIView):
    lookup_field = 'slug'
    lookup_url_kwarg = 'genre_slug'
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class GenreListAPIView(ListAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


# ReviewCreateAPIView, ReviewDeleteAPIView, ReviewListAPIView, ReviewUpdateAPIView,


# class ReviewAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         book = Book.objects.get(slug=kwargs['book_slug'])
#         reviews = book.review_set.all()
#         return Response(ReviewSerializer(reviews, many=True).data)
#
#     def post(self, request, *args, **kwargs):
#         serializer = ReviewSerializer(data=request.data)
#         book = Book.objects.get(slug=kwargs['book_slug'])
#         # print(f'dir(book): {dir(book)}')
#         # print(f'ID: {book.id}')
#         # print(f"slug: {kwargs['book_slug']}")
#         data = {
#             # 'author': request.user.id
#             'author': User.objects.get(pk=1).id,
#             'book': book.id,
#             'created': datetime.datetime.now(),
#             'edited': datetime.datetime.now(),
#         }
#         # print(f'author: {book.author}')
#         # print(f'request data: {request.data}')
#         request.data.update(data)
#         print(f'updated request data: {request.data}')
#         # print(f'DATA: {serializer.data}')
#         serializer.is_valid(raise_exception=True)
#         print('we are here')
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



