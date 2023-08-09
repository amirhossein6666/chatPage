from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer


@api_view(['POST'])
def register(request):
    serialized_user = UserSerializer(data=request.data)
    if serialized_user.is_valid():
        serialized_user.save()
        return Response(serialized_user.data, status=status.HTTP_201_CREATED)
    return Response(serialized_user.errors, status=status.HTTP_400_BAD_REQUEST)

