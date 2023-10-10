from django.urls import path
from . import api_views
urlpatterns = [
    path("sign_up/",api_views.signUpUser,name="sign-up")
]
