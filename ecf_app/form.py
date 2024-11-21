from .models import Offer, Competition
from django import forms

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = '__all__'
        
        widgets = {
          'description': forms.Textarea(attrs={'rows':4}),
        }
        
class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = '__all__'
        
        widgets = {
          'description': forms.Textarea(attrs={'rows':4}),
        }
        
class UpdateCompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = '__all__'
        
        widgets = {
          'description': forms.Textarea(attrs={'rows':4}),
        }
        
