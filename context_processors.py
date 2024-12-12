# context processors afin de rendre accessible cart dans tous les templates

from ecf_app.models  import Cart

def custom_data(request):
    cart = Cart.objects.get(user = request.user)
    return {'cart': cart}