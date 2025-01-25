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
from .form import RegisterCustomerForm, ProfileForm

from .models import Profile
from django.http import JsonResponse



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
        messages.success(request, f'Votre compte a été activé, pour pouvez vous authentifier actuelement... ensuite remplissez votre profil')
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
            
            # on créer un profil
            Profile.objects.create(user=user)
            
            # email content
            email_subject="Activer votre compte"
            message = render_to_string('account/activate.html', {
            'user ': user,
            'domain':'https://ecf-django.onrender.com',
            # encoder le user.pk
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            # generer un token pour le user.pk
            # en utilisant token.py avec 'six'
            'token': generate_token.make_token(user)
            })
            
              # send mail
            email_from = 'no-reply@test.test'
            recipient_list = [user.email]

            send_mail(email_subject, message, email_from, recipient_list)
            
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
            profile = Profile.objects.get(user= request.user)
            if profile.address == '': 
                messages.success(request,request.user.profile.address)
                return redirect('user-profile', pk=request.user)
            else:
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


#  --- PROFIL --- 
def edit_profile(request, pk):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profil modifié')
            return redirect('user_profile', pk=request.user)
            
        else:
            messages.warning(request,form.errors)
            return redirect('user_profile', pk=request.user)
    else:
        form = ProfileForm(instance=profile)
        context = {'form': form}
        return render(request, 'account/edit_profile.html', context)
   
def user_profile(request, pk):
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'account/user_profile.html', context)

# donnée bancaire d'un user est valable en json et qui seront requettés via ajax lors du paiement afin de vérifier les informations de l'utilisateur
def list_profile(request):
    profiles = Profile.objects.all()
    User = get_user_model()
    users = User.objects.all()


    context = {'profiles': profiles}
    
    profile_values = Profile.objects.values()
    user_values = User.objects.values()

    
    profile_data = list(profile_values)
    user_data = list(user_values)
    
    # retourner un end point en json
    return JsonResponse({
        'profile_data': profile_data,
        'user_data': user_data,
    })
    