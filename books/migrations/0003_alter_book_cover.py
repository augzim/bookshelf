# Generated by Django 4.1.3 on 2022-12-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_review_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Softcover'), (1, 'Hardcover Case Wrap'), (2, 'Hardcover Dust Jacket')], verbose_name='Book Cover'),
        ),
    ]
