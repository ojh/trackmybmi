from rest_framework import serializers

from .models import Measurement


class MeasurementSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Measurement
        fields = ('user', 'date', 'height', 'weight')
