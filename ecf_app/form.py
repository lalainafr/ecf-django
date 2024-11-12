from .models import Offer
from django import forms

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = '__all__'
        
        widgets = {
          'description': forms.Textarea(attrs={'rows':4}),
        }
        
