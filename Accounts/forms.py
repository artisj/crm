from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django import forms
from .models import Order


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        # order of the list will show in the display
        fields = ['username', 'email', 'password1', 'password2']

#Use a class for each form to be created
# the meta just overides the base ModelForm class
class OrderForm(ModelForm):
    class Meta:
        model = Order
        # special method to take all the created fields from the created
        # model class
        fields = '__all__'