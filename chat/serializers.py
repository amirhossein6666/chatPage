from rest_framework import serializers
from .models import publicMessage

class publicMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = publicMessage
        fields = ['title', 'author', 'body']