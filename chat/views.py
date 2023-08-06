from django.shortcuts import render
from rest_framework.generics import ListAPIView , CreateAPIView
from .serializers import messageSerializers
from .models import publicMessage
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework import authentication, permissions

class messageListApiView(ListAPIView):
    queryset = publicMessage.objects.all()
    serializer_class = messageSerializers

class messageCreateApiView(LoginRequiredMixin, CreateAPIView):
    queryset =publicMessage.objects.all()
    serializer_class = messageSerializers
    authentication_classes = [authentication.TokenAuthentication]     
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)