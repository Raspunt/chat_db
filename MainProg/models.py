from statistics import mode
from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    
    autor = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return self.autor.username


class Chat(models.Model):
    title = models.CharField(max_length=200)
    disc = models.TextField(blank=True)
    messages = models.ManyToManyField(Message, blank=True)

    def __str__(self):
        return self.title



