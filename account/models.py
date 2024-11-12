from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# create user model here
class User(AbstractUser):
    last_name= models.CharField( max_length=50, null=True, blank=True)
    first_name= models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    userUid = models.UUIDField(default=uuid.uuid4)
    
    def __str__(self) -> str:
        return str(self.last_name) + ' ' +  str(self.first_name)


