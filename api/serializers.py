from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ['date_creation']

    def validate_titre(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Le titre doit faire au moins 5 caractères.")
        return value