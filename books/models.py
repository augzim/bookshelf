from datetime import date, timedelta

from django.db import models
from django.contrib.auth import get_user_model
from django.core import validators
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey('Author', on_delete=models.PROTECT)
    pages = models.PositiveSmallIntegerField()
    genre = models.ManyToManyField('Genre')
    publisher = models.CharField(max_length=100)
    description = models.TextField(max_length=5000, )
    price = models.DecimalField(max_digits=8, decimal_places=2, help_text='Price in USD')
    quantity = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='amount')

    LANGUAGES = (
        ('en', 'English'),
        ('fr', 'French'),
        ('de', 'German'),
        ('el', 'Greek'),
        ('it', 'Italian'),
        ('ru', 'Russian'),
        ('es', 'Spanish'),
    )

    language = models.CharField(max_length=2, choices=LANGUAGES, default='en')

    COVERS = (
        (0, 'Softcover'),
        (1, 'Hardcover Case Wrap'),
        (2, 'Hardcover Dust Jacket'),
    )

    cover = models.PositiveSmallIntegerField(choices=COVERS, verbose_name='Book Cover')

    isbn = models.CharField(
        max_length=17,
        verbose_name='ISBN-10/13',
        help_text='Correct ISBN format: (XXX-)XXXXXXXXXX. If prefix exists remove parenthesis',
        db_index=True,
        validators=[
            validators.RegexValidator(
                regex=r'(?:\d{3}-)?\d{10}',
                message='Please, see correct ISBN format above',
            )
        ],
    )

    def __str__(self):
        return self.title

    def is_available(self):
        return f'YES' if self.quantity else \
            f'Expected Time of Receipt: {str(date.today() + timedelta(days=14))}'

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['title', ]


class Review(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    description = models.TextField(max_length=5000, blank=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    MARKS = (
        (1, 'awful'),
        (2, 'bad'),
        (3, 'average'),
        (4, 'good'),
        (5, 'excellent'),
    )

    mark = models.PositiveSmallIntegerField(choices=MARKS, verbose_name='Rating')

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.book.pk})

    class Meta:
        ordering = ['-edited']


class Author(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=3000, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['name']


class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['name']
