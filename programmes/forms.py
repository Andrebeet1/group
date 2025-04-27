from django import forms
from django.contrib.auth.models import User
from .models import Programme, Activite

class ProgrammeForm(forms.ModelForm):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")

    class Meta:
        model = Programme
        fields = ['nom', 'annonce']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Ce nom d'utilisateur est déjà utilisé.")
        return username

class LoginSousAdminForm(forms.Form):
    programme = forms.ModelChoiceField(queryset=Programme.objects.all())
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

from django import forms
from .models import Activite

class ActiviteForm(forms.ModelForm):
    class Meta:
        model = Activite
        fields = ['numero', 'jour_date', 'tutaingiliya', 'mhubiri', 'kiongozi', 'mutangazaji']
        widgets = {
            'numero': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'N°'}),
            'jour_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jour & Date'}),
            'tutaingiliya': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tutaingiliya'}),
            'mhubiri': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mhubiri'}),
            'kiongozi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kiongozi'}),
            'mutangazaji': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mutangazaji'}),
        }
        labels = {
            'numero': 'Numéro',
            'jour_date': 'Jour et Date',
            'tutaingiliya': 'Tutaingiliya',
            'mhubiri': 'Mhubiri',
            'kiongozi': 'Kiongozi',
            'mutangazaji': 'Mutangazaji',
        }
