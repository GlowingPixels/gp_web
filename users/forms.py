from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.', required=True)
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Minimum 8 special and alphanumeric characters.")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
 