from django.urls import path, include
from app1.views import movie_list, movie_details
urlpatterns = [
    path('list/', movie_list, name = 'movie-list'),
    path('detail/<int:pk>/', movie_details),
]