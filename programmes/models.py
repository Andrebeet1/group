from django.db import models
from django.contrib.auth.models import User

class Programme(models.Model):
    nom = models.CharField(max_length=255)
    sous_admin = models.OneToOneField(User, on_delete=models.CASCADE)
    annonce = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

class Activite(models.Model):
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE, related_name='activites')
    numero = models.PositiveIntegerField()
    jour_date = models.CharField(max_length=100)
    tutaingiliya = models.CharField(max_length=200)
    mhubiri = models.CharField(max_length=100)
    kiongozi = models.CharField(max_length=100)
    mutangazaji = models.CharField(max_length=100)

    def __str__(self):
        return f"Activité {self.numero} - {self.programme.nom}"
