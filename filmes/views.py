from django.http import HttpResponse
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views import generic
from .models import Filme
from .serializers import FilmeSerializer
from django.http import Http404

# HEROKU APPLICATION URL: https://cinelist-backend.herokuapp.com/minhalista/ 

@api_view(['GET', 'POST'])
def api_filme(request, filme_id):
    # try:
    #     print("passei no try")
    #     filme = Filme.objects.get(id=filme_id)
    # except Filme.DoesNotExist:
    #     raise Http404()

    filme = Filme.objects.get(id=filme_id)
    
    if request.method == 'POST':
        new_filme_data = request.data
        # FilmeSerializer.create(new_filme_data)
        filme.title = new_filme_data['title']
        filme.description = new_filme_data['description']
        filme.year = new_filme_data['year']
        filme.cast = new_filme_data['cast']
        filme.director = new_filme_data['director']
        filme.save()

        serializer = FilmeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      

    elif request.method == 'GET':
        serialized_filme = FilmeSerializer(filme)
        return Response(serialized_filme.data)

    elif request.method == 'PUT':
        serializer = FilmeSerializer(filme, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        filme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# {
#   "title": "Game of Trones",
#   "description": "Drama, Adventure, Fantasy",
#   "year": 2011,
#   "cast": "Emily Clark, Kit, ...",
#   "director" : "Alan Taylor"
# }
