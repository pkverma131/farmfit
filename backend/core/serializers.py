from rest_framework import serializers
from .models import Crop, STORAGE_TIME_UNIT_CHOICES, UNIT_CHOICES


class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = ['name', 'description', 'yield_ph', 'maturity_time']