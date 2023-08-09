from rest_framework import serializers
from .models import publicMessage, privateMessage

class publicMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = publicMessage
        fields = ['title', 'author', 'body']

class privateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = privateMessage
        fields= ['title', 'body', 'author', 'receiver']