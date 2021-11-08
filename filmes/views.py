from django.http import HttpResponse
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Filme
from .serializers import FilmeSerializer
from django.http import Http404

# class FilmeView(generics.CreateAPIView):
#     queryset = Filme.objects.all()
#     def get_serializer_class(self):
#         return FilmeSerializer

@api_view(['GET', 'POST'])
def api_filme(request, filme_id):
    try:
        filme = Filme.objects.get(id=filme_id)
    except Filme.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        new_filme_data = request.data
        filme.title = new_filme_data['title']
        filme.description = new_filme_data['description']
        filme.year = new_filme_data['year']
        filme.cast = new_filme_data['cast']
        filme.director = new_filme_data['director']
        filme.save()

    serialized_filme = FilmeSerializer(filme)
    return Response(serialized_filme.data)