from rest_framework import serializers
from .models import Filme

class FilmeSerializer(serializers.Serializer):
    class Meta:
        model = Filme
        fields = ['id' , 'title', 'description', 'year', 'cast', 'director']

