from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import CustomUser
from core.utils.customer_data import read_customer_data


class SignUpForm(UserCreationForm):
    customers = forms.ChoiceField(choices=read_customer_data(), required=True, label='Empresa')

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'customers', 'password1', 'password2')
