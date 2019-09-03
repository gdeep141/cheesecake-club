from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        """ Nested namespace for configurations. """
        model = User  # Model this form interacts with.
        fields = ['username', 'email', 'password1', 'password2'] # Fields we want in order.
