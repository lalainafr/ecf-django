from django.shortcuts import render


def home(request):

    return render(request, 'ecf_app/home.html')