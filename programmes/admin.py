from django.contrib import admin
from .models import Programme, Activite

@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'sous_admin', 'date_creation')
    search_fields = ('nom', 'sous_admin__username')

@admin.register(Activite)
class ActiviteAdmin(admin.ModelAdmin):
    list_display = ('programme', 'numero', 'jour_date', 'tutaingiliya', 'mhubiri', 'kiongozi', 'mutangazaji')
    list_filter = ('programme',)
    search_fields = ('programme__nom', 'jour_date', 'mhubiri')
