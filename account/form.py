from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from account.models import Profile

User = get_user_model()

class RegisterCustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['last_name','first_name', 'email', 'password1', 'password2']



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        
        widgets = {
          'address': forms.Textarea(attrs={'rows':4}),
        }