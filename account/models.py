from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# create user model here
class User(AbstractUser):
    last_name = models.CharField(max_length=50, default='prénom')
    first_name= models.CharField(max_length=50, default='nom')
    email = models.EmailField(unique=True)
    userUid = models.UUIDField(default=uuid.uuid4)
    
    def __str__(self) -> str:
        return (self.last_name) + ' ' + self.first_name

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    address = models.TextField()
    # les informations suivantes servent juste pour la 'SIMULATION DE PAIEMENT'
    # dans la vraie vie les informations confidentielles ne sont pas stockées ainsi
    bankName = models.CharField(max_length=50)
    accountNb = models.CharField(max_length=50)
    accountAvalable = models.FloatField(default=100.00, blank=True, null=True)
    