from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# create user model here
class User(AbstractUser):
    last_name = models.CharField(max_length=50, default='')
    first_name= models.CharField(max_length=50, default='')
    email = models.EmailField(unique=True)
    userUid = models.UUIDField(default=uuid.uuid4)
    
    def __str__(self) -> str:
        return (self.last_name) + ' ' + self.first_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)
    birthdate = models.DateTimeField(blank=True, null=True)
    # les informations suivantes servent juste pour la 'SIMULATION DE PAIEMENT'
    # dans la vraie vie les informations confidentielles ne sont pas stockées ainsi
    bankName = models.CharField(max_length=50, blank=True, null=True)
    accountNb = models.CharField(max_length=50, blank=True, null=True)
    accountAvailable = models.FloatField(default=100)    
    
    def __str__(self) -> str:
        return (self.user.last_name) + ' ' + self.user.first_name
