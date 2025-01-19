from .models import Javobgar
from rest_framework import serializers
class JavobgarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Javobgar
        fields = '__all__'