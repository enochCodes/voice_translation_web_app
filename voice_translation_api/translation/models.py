from django.db import models
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class TranslatedMessage(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    original_text = models.TextField()
    translated_text = models.TextField()
