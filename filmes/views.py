from django.http import HttpResponse
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views import generic
from .models import Filme
from .serializers import FilmeSerializer
from django.http import Http404

# HEROKU APPLICATION URL: https://cinelist-backend.herokuapp.com/minhalista/ 

@api_view(['GET','POST','PUT','UPDATE','DELETE'])
def api_filme(request, filme_id):
    try:
        filme = Filme.objects.get(id=filme_id)
    except Filme.DoesNotExist:
        raise Http404()
    
    if request.method == 'POST' or request.method == 'UPDATE':
        new_filme_data = request.data
        filme.title = new_filme_data['title']
        filme.description = new_filme_data['description']
        filme.year = new_filme_data['year']
        filme.cast = new_filme_data['cast']
        filme.director = new_filme_data['director']
        filme.save()

        serialized_filme = FilmeSerializer(data=request.data)
        return Response(serialized_filme.data)

    elif request.method == 'GET':
        serialized_filme = FilmeSerializer(filme)
        return Response(serialized_filme.data)

    elif request.method == 'DELETE':
        filme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def api_minhalista(request):
    
    if request.method == 'POST':
        filme = Filme()
        new_filme_data = request.data
        filme.title = new_filme_data['title']
        filme.description = new_filme_data['description']
        filme.year = new_filme_data['year']
        filme.cast = new_filme_data['cast']
        filme.director = new_filme_data['director']
        filme.save()
      
    filmes = Filme.objects.all()
    print(filmes)
    serialized_filme = FilmeSerializer(filmes, many=True)
    return Response(serialized_filme.data)
    
def gotominhalista(request):
    return HttpResponse("Olá! Visite a lista de filmes na url: https://cinelist-backend.herokuapp.com/minha-lista/ ")