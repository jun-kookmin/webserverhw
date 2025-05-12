from django.urls import path
from .views import hello_api, receive_post

urlpatterns = [
    path('hello/', hello_api),
    path('post/', receive_post),
]