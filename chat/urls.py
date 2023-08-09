from django.urls import path
from .views import publicMessageList, publicMessageCreate

urlpatterns = [
    path('', publicMessageList, name= 'public_message_list'),
    path('create/', publicMessageCreate, name='public_message_create')
]
