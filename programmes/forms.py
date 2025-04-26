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

class ActiviteForm(forms.ModelForm):
    class Meta:
        model = Activite
        fields = ['numero', 'jour_date', 'tutaingiliya', 'mhubiri', 'kiongozi', 'mutangazaji']
