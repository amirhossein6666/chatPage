from django.db import models
from django.contrib.auth.models import User


class publicMessage(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=150)
    author = models.ForeignKey(User, related_name='public_message_author', on_delete=models.CASCADE)

    def __str__(self) :
        return self.title
class privateMessage(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=150)
    author= models.ForeignKey(User, related_name='private_message_author', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User,related_name='private_message_receiver', on_delete=models.CASCADE)

    def __str__(self):
        return self.title