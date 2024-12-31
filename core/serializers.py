from rest_framework import serializers
from .models import Concession, Vehicule

class ConcessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concession
        exclude = ['numero_siret']  # Exclut numero_siret

class VehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicule
        fields = '__all__'  # Inclut tous les champs
