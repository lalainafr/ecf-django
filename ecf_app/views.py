from django.shortcuts import render


def home(request):
    return render(request, 'ecf_app/home.html')


def offer(request):
    return render(request, 'ecf_app/offer.html')