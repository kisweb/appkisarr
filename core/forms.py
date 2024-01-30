from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import get_user_model
from .models import Contact


class RegisterForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder": "Entrer votre email"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Entrer votre username"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder": "Saisir un mot de passe"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder": "Confirmer le mot de passe"}))
    class Meta:
        model = get_user_model() 
        fields = ["email", "username", "password1", "password2"]
        


class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Prénoms"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Nom de famille"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Votre pseudo"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder": "Votre Email"}))
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control", "placeholder": "Télécharger une image"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Votre adresse"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter Tépéphone"}))
    bio = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder": "Décrivez vous en quatre mots ..."}))
    role = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Votre fonction"}))
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "username", "email", "address", "bio", "phone", "profile_pic"]
        
        
class ContactForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder": "Saisir votre email"}))
    name = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder": "Saisir votre nom complet"}))
    message = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder": "Saisir votre message"}))
    class Meta:
        model=Contact 
        fields = ["email", "name", "message"]