from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import publicMessage, privateMessage
from .serializers import publicMessageSerializer, privateMessageSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

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

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def publicMessageDelete(request, id):
    try:
        public_message= publicMessage.objects.get(pk=id)
    except publicMessage.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)        
    
    if request.method == 'DELETE':
        public_message.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def privateMessageList(request):
    private_messages = privateMessage.objects.filter(receiver= request.user)
    serialized_private_message = privateMessageSerializer(private_messages , many= True)
    return Response(serialized_private_message.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes({IsAuthenticated})
def privateMessageCreate(request):
    if request.method == 'POST':
        message_receiver = User.objects.get(username=request.data['receiver_username'])
        private_message = {
            'title' : request.data['title'],
            'body' : request.data['body'],
            'author' : request.user.id,
            'receiver' : message_receiver.id
        }
        serializedPrivateMessage = privateMessageSerializer(data=private_message)
        if serializedPrivateMessage.is_valid():
            serializedPrivateMessage.save()
            return Response(serializedPrivateMessage.data, status=status.HTTP_201_CREATED)
        return Response(serializedPrivateMessage.errors, status=status.HTTP_400_BAD_REQUEST)

