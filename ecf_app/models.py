from django.db import models

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


    