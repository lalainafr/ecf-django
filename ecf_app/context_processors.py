# context processors afin de rendre accessible cart dans tous les templates
# Disable django context processor in django-admin pages
from ecf_app.models  import Cart
from account.models import Profile
from django.urls import reverse

def custom_data(request):
    if request.path.startswith(reverse('admin:index')):
        return {}
    else:
        if request.user.is_authenticated:
            try:
                cart = Cart.objects.get(user = request.user)
                return {'cart': cart}
            except Cart.DoesNotExist:
                cart = None
            
            try:
                profile = Profile.objects.get(user = request.user)
                return {'profile': profile}
            except Cart.DoesNotExist:
                profile = None
        return {}