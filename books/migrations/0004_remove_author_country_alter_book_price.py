# Generated by Django 4.1.3 on 2022-12-02 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='country',
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Price in USD', max_digits=8),
        ),
    ]
