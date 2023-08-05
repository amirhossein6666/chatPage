from .models import publicMessage
from rest_framework import serializers

class messageSerializers(serializers.ModelSerializer):
    class Meta:
        model = publicMessage
        fields = ['sender' , 'messageText']