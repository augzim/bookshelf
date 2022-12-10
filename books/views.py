from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .forms import ReviewForm
from .models import Author, Book, Genre, Review


class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(book_id=context['book'].pk)
        return context


class BookListView(ListView):
    paginate_by = 10
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        return context


class GenreDetailView(DetailView):
    model = Genre

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(genre=context['genre'].pk)
        return context


class GenreListView(ListView):
    model = Genre


class AuthorDetailView(DetailView):
    model = Author


class AuthorListView(ListView):
    paginate_by = 10
    model = Author


class ReviewCreateView(LoginRequiredMixin, CreateView):
    form_class = ReviewForm
    login_url = 'login'
    template_name = 'books/review_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.book = Book.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = 'login'
    model = Review
    template_name = 'books/review_delete.html'

    def get_success_url(self):
        obj = self.get_object()
        return reverse_lazy('book_detail', kwargs={'pk': obj.book.pk})

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = ReviewForm
    login_url = 'login'
    model = Review
    template_name = 'books/review_edit.html'

    def get_success_url(self):
        obj = self.get_object()
        return reverse_lazy('book_detail', kwargs={'pk': obj.book.pk})

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
