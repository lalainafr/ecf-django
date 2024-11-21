from django.shortcuts import render
from .form import OfferForm
from .models import Offer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'ecf_app/home.html')

def competition(request):
    return render(request, 'ecf_app/competition.html')

# --- OFFER ---
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

        
        