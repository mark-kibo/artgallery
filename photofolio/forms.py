from django.forms import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, ArtImages


class RegisterForm(UserCreationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets={
            'username':forms.TextInput(attrs={'name':'type', 'class': 'form-username'}),
            'password1':forms.TextInput(attrs={'class': 'form-password'}),
            'password2':forms.TextInput(attrs={'class': 'form-password1'})
        }


photo_choices = (('nature','nature'), ('adventure','adventure'),
 ('people','people'),  ('travel', 'travel'))

class ArtImagesForm(forms.ModelForm):
    class Meta:
        model = ArtImages
        fields = "__all__"
        widgets={
            'type':forms.Select(choices=photo_choices, attrs={'name':'type', 'class': 'form-control'}),
            'art_image':forms.FileInput(attrs={'multiple':'multiple', 'name':'img', 'class': 'form-control'})
        }