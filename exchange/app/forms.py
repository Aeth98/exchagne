from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order

class Register(UserCreationForm):
    email = forms.CharField(max_length=100,)
    class Meta:
        model = User
        fields =["username", "email", "password1", "password2"]

class PlaceOrder(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['price', 'quantity']