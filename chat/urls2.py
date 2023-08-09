from django.urls import path
from .views import privateMessageList, privateMessageCreate, privateMessageDelete
urlpatterns = [ 
    path('', privateMessageList, name='private_message_list'),
    path('create/', privateMessageCreate, name='private_message_create'),
    path('delete/<int:id>', privateMessageDelete, name='private_message_delete') 
]