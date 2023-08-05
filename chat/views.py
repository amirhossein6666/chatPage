from django.shortcuts import render
from rest_framework.generics import ListAPIView 
from .serializers import messageSerializers
from .models import publicMessage

class messageListApiView(ListAPIView):
    queryset = publicMessage.objects.all()
    serializer_class = messageSerializers