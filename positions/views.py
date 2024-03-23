
from .models import Positions
from rest_framework import viewsets, permissions
from .serializers import PositionsSerializer

class PositionsViewSet(viewsets.ModelViewSet):
    queryset=Positions.objects.all().order_by('id')
    serializer_class=PositionsSerializer
    permission_classes=[permissions.AllowAny]