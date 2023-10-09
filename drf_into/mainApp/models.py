from django.db import models

# Create your models here.
class BookModel(models.Model):
    class Genre(models.TextChoices):
        fiction="FIC","Fiction"
        fantasy="FANT","Fantasy"
        non_fiction="NON-FIC","Non-fiction"
    book_title=models.CharField(max_length=30)
    book_author=models.CharField(max_length=20)
    book_genre=models.CharField(choices=Genre.choices, max_length=15)
