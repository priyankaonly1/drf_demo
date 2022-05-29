from django.urls import path, include
from app1.api.views import movie_list, movie_details
urlpatterns = [
    path('lists/', movie_list),
    path('<int:pk>', movie_details),
]
