# context processors afin de rendre accessible cart dans tous les templates
# Disable django context processor in django-admin pages
from ecf_app.models  import Cart
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
        return {}