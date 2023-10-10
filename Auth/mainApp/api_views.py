import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSignUpSerializer
@api_view(["POST"])
def signUpUser(request):
    if request.method=="POST":
        serializer=UserSignUpSerializer(data=request.data)