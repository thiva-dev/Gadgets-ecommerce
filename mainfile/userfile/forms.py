from django import forms
from .models import User, Product

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['username','email','password']
        widgets = {
            'password':forms.PasswordInput()
        }

#login form

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'img', 'price', 'des']
