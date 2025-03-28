from django.db import models
from django.conf import settings 
# Create your models here.

class Room(models.Model):
    #Proprietario da sala de chat, muitos-para-um,ou seja, um usuário pode ter várias salas, mas cada sala pertence a apenas um usuário.
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    messages = models.ManyToManyField('Message',blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Message(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete = models.CASCADE,
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}: {self.text}" 
