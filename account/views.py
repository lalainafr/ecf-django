from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import *
from django.core.mail import send_mail
from django.views.generic import View

# token - mail confirmation import
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .token import TokenGenerator, generate_token
from django.utils.encoding import force_bytes, force_str
from django.conf import settings
from django.contrib.auth import get_user_model
from .form import RegisterCustomerForm


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        # on decode le pk et on le compare si ca correspond à l'id du user
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as identifier:
        user = None
        
    # on decode le token et le compare par rapport au token generé   
    if user is not None and generate_token.check_token(user, token):
        user.is_active = True
        user.save()     
        messages.success(request, f'Votre compte a été activé, pour pouvez vous authentifier actuelement..')
        return redirect('login') 
    return render (request, 'account/activate_fail.html')  
    


# register customer
def register_user(request):
    if request.method == 'POST':
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            user.is_active = False
            user.save()
            
            # email content
            email_subject="Activer votre compte"
            message = render_to_string('account/activate.html', {
            'user ': user,
            'domain':'127.0.0.1:8000',
            # encoder le user.pk
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            # generer un token pour le user.pk
            # en utilisant token.py avec 'six'
            'token': generate_token.make_token(user)
            })
            
              # send mail
            email_from = 'lalaina@myself.com'
            recipient_list = [user.email]

        
            send_mail(email_subject, message, email_from, recipient_list)
            
            # messages.success(request, 'Account created successfully. please log in')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('register_user')
    else:
        form = RegisterCustomerForm()
        context = {'form': form}
        return render(request, 'account/register_user.html', context)
   
# login
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.warning(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'account/login.html')

# logout
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')