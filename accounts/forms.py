from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class UserRegisterForm(UserCreationForm):
    phone = forms.CharField(label="Утасны дугаар",
                            widget=forms.NumberInput(attrs={'maxlength': 8}))

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'phone',
                  'address', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    phone = forms.CharField(label='Утасны дугаар',
                            widget=forms.NumberInput(attrs={'maxlength': 8}))

    class Meta:
        model = User
        fields = ('phone', 'password')
