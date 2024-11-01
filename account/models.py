from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# create user model here
class User(AbstractUser):
    last_name= models.CharField(null=True, blank=True)
    first_name= models.CharField(null=True, blank=True)
    email = models.EmailField(unique=True)
    userUid = models.UUIDField(default=uuid.uuid4)
   
    def __str__(self):
        return self.last_name + self.first_name