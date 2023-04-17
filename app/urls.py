from django.urls import path
from .views import liked_pages, unlike_pages

urlpatterns = [
    path('liked_pages/', liked_pages, name="liked_pages"),
    path('unlike_pages/', unlike_pages, name="unlike_pages"),
]
