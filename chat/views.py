from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import publicMessage
from .serializers import publicMessageSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def publicMessageList(request):
    publicMessages = publicMessage.objects.all()
    serializedPublicMessage = publicMessageSerializer(publicMessages, many= True)
    return Response(serializedPublicMessage.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def publicMessageCreate(request):
    if request.method == 'POST':
        public_message = {
            'title' : request.data['title'],
            'body' : request.data['body'],
            'author' : request.user.id
        }
        serializedPublicMessage = publicMessageSerializer(data=public_message)
        if serializedPublicMessage.is_valid():
            serializedPublicMessage.save()
            return Response (serializedPublicMessage.data, status=status.HTTP_201_CREATED)
        return Response(serializedPublicMessage.errors, status=status.HTTP_400_BAD_REQUEST)