# Generated by Django 4.1.3 on 2022-12-02 08:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(blank=True, max_length=100, verbose_name='Country')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('pages', models.PositiveSmallIntegerField()),
                ('publisher', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=5000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='amount')),
                ('language', models.CharField(choices=[('en', 'English'), ('fr', 'French'), ('de', 'German'), ('el', 'Greek'), ('it', 'Italian'), ('ru', 'Russian'), ('es', 'Spanish')], default='en', max_length=2)),
                ('cover', models.PositiveSmallIntegerField(choices=[(0, 'Softcover'), (1, 'Hardcover Case Wrap'), (2, 'Hardcover Dust Jacket')], max_length=1, verbose_name='Book Cover')),
                ('isbn', models.CharField(db_index=True, help_text='Correct ISBN format: (XXX-)X-XXXXXX-XX-X.\nIf prefix exists remove parenthesis', max_length=17, validators=[django.core.validators.RegexValidator(message='Please, see correct ISBN format above', regex='(?:\\d{3}-)?\\d-\\d{6}-\\d{2}-\\d')], verbose_name='ISBN-10/13')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.author')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('description', models.TextField(blank=True, max_length=5000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('mark', models.PositiveSmallIntegerField(choices=[(1, 'awful'), (2, 'bad'), (3, 'average'), (4, 'good'), (5, 'excellent')], max_length=1, verbose_name='Rating')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='books.genre'),
        ),
    ]