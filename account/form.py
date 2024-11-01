from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class RegisterCustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['last_name','first_name', 'email', 'password1', 'password2']