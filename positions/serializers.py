from .models import Positions
from rest_framework import serializers

class PositionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Positions
        fields=('id', 'name', 'position')