from rest_framework import serializers

from .models import Measurement


class MeasurementSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    date = serializers.DateField()
    height = serializers.DecimalField(max_digits=3, decimal_places=2)
    weight = serializers.DecimalField(max_digits=5, decimal_places=2)
