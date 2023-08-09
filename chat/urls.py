from django.urls import path
from .views import publicMessageList, publicMessageCreate, publicMessageDelete

urlpatterns = [
    path('', publicMessageList, name= 'public_message_list'),
    path('create/', publicMessageCreate, name='public_message_create'),
    path('delete/<int:id>', publicMessageDelete, name='public_message_delete')
]
