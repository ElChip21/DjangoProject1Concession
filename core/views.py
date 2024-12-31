from rest_framework.viewsets import ModelViewSet
from .models import Concession, Vehicule
from .serializers import ConcessionSerializer, VehiculeSerializer

class ConcessionViewSet(ModelViewSet):
    queryset = Concession.objects.all()
    serializer_class = ConcessionSerializer

class VehiculeViewSet(ModelViewSet):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer
