from django.contrib import admin
from .models import publicMessage, privateMessage
admin.site.register(publicMessage)
admin.site.register(privateMessage)
