from django.urls import path
from . import api_views
urlpatterns = [
    path("api/first_api_view/", api_views.theBooks,name="all_books"),
    path("api/add_new_book/",api_views.add_Book,name="add_book")
]
