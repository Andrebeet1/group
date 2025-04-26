from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('programme.urls')),  # Inclusion des URLs de l'app principale
]
