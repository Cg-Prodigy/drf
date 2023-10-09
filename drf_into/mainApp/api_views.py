from rest_framework.decorators import api_view

from rest_framework.response import Response
from mainApp.models import BookModel
from mainApp.serializers import BookSerializer


@api_view()
def theBooks(request):
    books=BookModel.objects.all()
    book_serializer=BookSerializer(books,many=True)
    return Response(book_serializer.data)
@api_view(["POST"])
def add_Book(request):
    if request.POST:
        data=BookSerializer(data=request.data)
        if data.is_valid():
            data.save()
    return Response({"data":data.data})