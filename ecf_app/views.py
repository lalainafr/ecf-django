from django.shortcuts import render, redirect
from .form import OfferForm, CompetitionForm, UpdateCompetitionForm, OfferChoiceForm
from .models import Offer, Competition, Cart, Order
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse



def home(request):
    return render(request, 'ecf_app/home.html')

def competition(request):
    return render(request, 'ecf_app/competition.html')

# --- OFFER: crud + ajax ---
def offer(request):
    form = OfferForm()
    offers = Offer.objects.all().order_by('id')
    context = {'form': form, 'offers': offers}
    return render(request, 'ecf_app/offer.html', context)

# create
# preventing csrf attack
@csrf_exempt
def data_save(request):
    if request.method =='POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            # get the SID frmo 'stuid' the EDIT ajax
            # eviter de créer une nouvelle instance avec EDIT
            sid = request.POST.get('stuid')
            
            # take value from the AJAX --> 'name, desdcription, nbPers, discount' --> to update de bdd   
            name = request.POST['name']
            description = request.POST['description']
            nbPers = request.POST['nbPers']
            discount = request.POST['discount']

            # create an instance of Student
                #  SID récupéré à partir de AJAX --> mydata = {sid:id}
                # si on a un SID on le met la valeur dans ID

            if(sid == ''):
                offre = Offer(name=name, description=description, nbPers=nbPers, discount = discount)
            else:
                # on assigne a id le sid
                offre = Offer(id= sid, name=name, description=description, nbPers=nbPers, discount = discount)
                 
            offre.save()
            
            # --> PUT INT THE TABLE INT THE RIGHT SIDE THE DATA REVEICED FROM THE AJAX CALL
            # take the values of all student data in the database
            offer_values = Offer.objects.values()
            # convert it to python list
            offer_data = list(offer_values)
            
            # return to json as well the data converted as a python list
            return JsonResponse({'status': 'Data saved', 'offer_data': offer_data})
        else: 
            return JsonResponse({'status': 'Unable to save'})
    
    
@csrf_exempt
def data_delete(request):
    if request.method == 'POST':
        #  SID récupéré à partir de AJAX --> mydata = {sid:id}
        id = request.POST.get('sid')
        offre = Offer.objects.get(pk=id)
        offre.delete()
        return JsonResponse({'status':1})
    else: 
        return JsonResponse({'status':0})

@csrf_exempt
def data_edit(request):
    if request.method == 'POST':
        # récupérer le id à partir de l'appel AJAX
        id = request.POST.get('sid')

        offre = Offer.objects.get(pk=id)
        offer_data = {'id': offre.id, 'name': offre.name, 'description': offre.description, 'nbPers': offre.nbPers, 'discount': offre.discount}

        return JsonResponse(offer_data)

        
    
# ---  COMPETITION: crud ---
def create_competition(request):
    if request.method == 'POST':
        form = CompetitionForm(request.POST, request.FILES)
        # reuqest.FILES quand il y a un fochoer pou image dans le formulaire

        if form.is_valid():
            form.save()
            messages.success(request, 'La competition a été créée')
            return redirect('list_competition')
        else:

            messages.warning(request, {form})
            return redirect('home')

    else:
        form = CompetitionForm()
        context = {'form': form}
        return render(request, 'ecf_app/create_competition.html', context)

def list_competition(request):
    competitions = Competition.objects.all()
    context = {'competitions': competitions}
    return render(request, 'ecf_app/list_competition.html', context)

def edit_competition(request, pk):
    competition = Competition.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateCompetitionForm(request.POST, request.FILES, instance=competition)
        # reuqest.FILES quand il y a un fochoer pou image dans le formulaire

        if form.is_valid():
            form.save()
            messages.success(request, 'La competition a été modifiée')
            return redirect('list_competition')
        else:

            messages.warning(request, {form})
            return redirect('home')

    else:
        form = UpdateCompetitionForm(instance=competition)
        context = {'form': form}
        return render(request, 'ecf_app/update_competition.html', context)

    
def delete_competition(request, pk):
    competition = Competition.objects.get(pk=pk)
    competition.delete()
    return redirect('list_competition')

def detail_competition(request, pk):
    competition = Competition.objects.get(pk=pk)
    context = {'competition': competition}
    return render(request, 'ecf_app/detail_competition.html', context)


# --- CART ---
def add_to_cart(request, pk):
    user = request.user
    
    # --> récupérer la competition concernée à parti de son id
    # s'il existe on le récupère sinon on aura une erreur 404
    competition = get_object_or_404(Competition, pk=pk)
    
    # --> on récupére le CART (panier) appartenant à un utilisateur s'il existe sinon on le crée en associant le panier à l'utilisateur
    # retourne 2 elments: l'objet - un boolean pour savoir s'il l'objet a été crée ou non
    cart, _ = Cart.objects.get_or_create(user=user)
    # _ variable qui ne sera pas utilisée par la suite
    # ca ne nous interesse pas de savoir si le panier existe ou non
    # --> la competition sera créer qu'une seule fois dans le panier
    
        
    # si l'element existe dans le pânier de la bdd on l'incremente sinon on le rajoute dans le panier
    # On récupère ORDER qui est associée à un user et qui correspont à la competition concernée
    order, created = Order.objects.get_or_create(user=user, competition = competition)
    # order: l'objet
    # created: bool pour savoir si l'element a été crée ou non

    if created:
    # cela veut dire qu'il n'existe pas encore dans le panier, donc il faudra le créer (avec l'element qu'on a récupérer: 'order')   
        cart.orders.add(order)
    else:
    # created == false -> l'element existe déja > il faut juste incrementer sa quantité   
        order.quanity += 1
        order.save()      
    return redirect('detail_competition', pk=pk) 
    
def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    
    # choix de l'offre (formulaire)
    form = OfferChoiceForm()
    if request.method == 'POST':
        form = OfferChoiceForm(request.POST, instance=cart)
        if form.is_valid():
            form.save()
            return redirect('cart')
        else: 
            messages.warning(request, 'Something went wrong')
            return redirect('cart')
    else:
        form = OfferChoiceForm()
        cart = get_object_or_404(Cart, user=request.user)
    
        context = {'cart': cart, 'form': form}
        return render(request, 'ecf_app/cart.html', context)


   