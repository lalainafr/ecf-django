from django.contrib import admin
from ecf_app.models import  Order, Cart, Competition, Offer, Payment

admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Competition)
admin.site.register(Offer)
admin.site.register(Payment)