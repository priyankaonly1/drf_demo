from django.shortcuts import render
from django.http import JsonResponse
from app1.models import Movie

#complex query sert result ----> Python Dictionary ---> JSON Response
def movie_list(request):
    #query set objects
    movies = Movie.objects.all()[:1]
    # data = {
    #     'movies': list(movies.values())
    #     }

    
    return render(request ,'app1/main.html', {'context':movies})
    # return JsonResponse(data)

def movie_details(request,pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'name':movie.name,
        'description': movie.description,
        'active': movie.active
    }
    return JsonResponse(data)
