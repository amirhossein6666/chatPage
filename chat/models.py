from django.db import models
from django.contrib.auth.models import User

class publicMessage (models.Model):
    sender = models.ForeignKey(User , on_delete=models.CASCADE)
    messageText = models.TextField()