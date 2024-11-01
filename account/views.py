from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from .form import RegisterCustomerForm
User = get_user_model()

# register customer
def register_user(request):
    if request.method == 'POST':
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.username = var.email
            var.save()
            messages.success(request, 'Account created successfully. please log in')
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