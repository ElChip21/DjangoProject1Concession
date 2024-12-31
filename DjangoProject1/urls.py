"""
URL configuration for DjangoProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from core.views import ConcessionViewSet, VehiculeViewSet
from django.shortcuts import redirect

# Routeur principal pour les concessions
router = routers.SimpleRouter()
router.register(r'concessions', ConcessionViewSet)

# Routeur imbriqué pour les véhicules d'une concession
concession_router = routers.NestedSimpleRouter(router, r'concessions', lookup='concession')
concession_router.register(r'vehicules', VehiculeViewSet, basename='concession-vehicules')

urlpatterns = [
    path('', lambda request: redirect('/concessions/')),  # Redirige vers /concessions/
    path('', include(router.urls)),  # Inclut les routes principales pour 'concessions'
    path('', include(concession_router.urls)),  # Inclut les routes imbriquées pour 'vehicules'
]
