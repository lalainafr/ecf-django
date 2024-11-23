from django.db import models
from django.contrib.auth import get_user_model
import uuid


User = get_user_model()


class Offer(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    nbPers = models.IntegerField()
    discount = models.IntegerField()

    def __str__(self):
        return self.name
    

class Competition(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    place = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/competition/')    
    
    def __str__(self):
        return self.title


    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    quanity = models.IntegerField(default=1) 
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.competition.title)

class Cart(models.Model):
    cartUid = models.UUIDField(default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, blank=True, null=True)
           
    def __str__(self):
        return self.user.firstname + ' ' +  self.user.lastname 
