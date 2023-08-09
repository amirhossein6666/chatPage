from django.urls import path
from .views import privateMessageList, privateMessageCreate
urlpatterns = [ 
    path('', privateMessageList, name='private_message_list'),
    path('create/', privateMessageCreate, name='private_message_create')   
]