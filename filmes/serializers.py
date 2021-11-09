from rest_framework import serializers
from .models import Filme

class FilmeSerializer(serializers.Serializer):
    class Meta:
        model = Filme
        fields = ['id' , 'title', 'description', 'year', 'cast', 'director']

    def create(self, validated_data):
        filme = Filme(
            id=validated_data['id'],
            title=validated_data['title'],
            description=validated_data['description'],
            year=validated_data['year'],
            cast=validated_data['cast'],
            director=validated_data['director'],
        )
        
        filme.save()
        return filme

