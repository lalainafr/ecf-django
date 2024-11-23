from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# create user model here
class User(AbstractUser):
    lastname = models.CharField(max_length=50, default='prénom')
    firstname= models.CharField(max_length=50, default='nom')
    email = models.EmailField(unique=True)
    userUid = models.UUIDField(default=uuid.uuid4)
    
    def __str__(self) -> str:
        return (self.lastname) + ' ' + self.firstname

