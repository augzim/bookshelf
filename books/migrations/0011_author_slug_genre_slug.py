# Generated by Django 4.1.3 on 2022-12-10 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_alter_book_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(default='slug', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='genre',
            name='slug',
            field=models.SlugField(default='slug', max_length=255),
            preserve_default=False,
        ),
    ]
