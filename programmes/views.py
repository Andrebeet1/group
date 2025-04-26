from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Programme, Activite
from .forms import ProgrammeForm, ActiviteForm, LoginSousAdminForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def accueil(request):
    programmes = Programme.objects.order_by('-date_creation')[:8]
    return render(request, 'accueil.html', {'programmes': programmes})

def liste_programmes(request):
    programmes = Programme.objects.all()
    return render(request, 'liste_programmes.html', {'programmes': programmes})

def detail_programme(request, programme_id):
    programme = get_object_or_404(Programme, id=programme_id)
    activites = programme.activites.order_by('numero')
    return render(request, 'detail_programme.html', {'programme': programme, 'activites': activites})

def creer_programme(request):
    if request.method == 'POST':
        form = ProgrammeForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            programme = form.save(commit=False)
            programme.sous_admin = user
            programme.save()
            messages.success(request, "Programme créé avec succès !")
            return redirect('accueil')
    else:
        form = ProgrammeForm()
    return render(request, 'creer_programme.html', {'form': form})

def login_sous_admin(request):
    if request.method == 'POST':
        form = LoginSousAdminForm(request.POST)
        if form.is_valid():
            programme = form.cleaned_data['programme']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user and programme.sous_admin == user:
                login(request, user)
                request.session['programme_id'] = programme.id
                return redirect('dashboard')
            else:
                messages.error(request, "Identifiants invalides")
    else:
        form = LoginSousAdminForm()
    return render(request, 'login_sous_admin.html', {'form': form})

@login_required
def dashboard(request):
    programme_id = request.session.get('programme_id')
    programme = get_object_or_404(Programme, id=programme_id)
    activites = programme.activites.order_by('numero')
    return render(request, 'dashboard.html', {'programme': programme, 'activites': activites})

@login_required
def ajouter_activite(request):
    programme_id = request.session.get('programme_id')
    programme = get_object_or_404(Programme, id=programme_id)
    if programme.activites.count() >= 25:
        messages.error(request, "Vous avez déjà atteint 25 activités")
        return redirect('dashboard')

    if request.method == 'POST':
        form = ActiviteForm(request.POST)
        if form.is_valid():
            activite = form.save(commit=False)
            activite.programme = programme
            activite.save()
            return redirect('dashboard')
    else:
        form = ActiviteForm()
    return render(request, 'ajouter_activite.html', {'form': form})

@login_required
def modifier_activite(request, activite_id):
    activite = get_object_or_404(Activite, id=activite_id)
    if request.method == 'POST':
        form = ActiviteForm(request.POST, instance=activite)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ActiviteForm(instance=activite)
    return render(request, 'modifier_activite.html', {'form': form})

@login_required
def supprimer_activite(request, activite_id):
    activite = get_object_or_404(Activite, id=activite_id)
    activite.delete()
    return redirect('dashboard')

def deconnexion(request):
    logout(request)
    return redirect('accueil')
