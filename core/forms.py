from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.CharField(label='Email',widget=forms.TextInput(attrs={'placeholder':'Email'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
