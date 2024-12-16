from django.db import models
from django.contrib.auth import get_user_model
import uuid


User = get_user_model()


class Offer(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    nbPers = models.IntegerField(default=1)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class Competition(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    place = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/competition/')
    price = models.FloatField(default=0.00)    
    
    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.competition.title)

class Cart(models.Model):
    cartUid = models.UUIDField(default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, blank=True, null=True)
    total = models.FloatField(default=0.00)
    isPaid = models.BooleanField(default=False)
           
    def __str__(self):
        return self.user.first_name + ' ' +  self.user.last_name 


    # methode afin de rajouter l'offre selectionée dans le panier
    def add(self, offer):        
        self.offer = offer
        
    def getTotalOrders(self):
        return self.orders.count()
    

        
    