from rest_framework import serializers
from mainApp.models import BookModel
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookModel
        fields=["book_title","book_author","book_genre"]