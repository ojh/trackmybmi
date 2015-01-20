from rest_framework import serializers

from .models import User
from measurements.models import Measurement


class UserSerializer(serializers.HyperlinkedModelSerializer):
    measurements = serializers.HyperlinkedRelatedField(
                        queryset=Measurement.objects.all(),
                        view_name='measurement-detail',
                        many=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'measurements')
