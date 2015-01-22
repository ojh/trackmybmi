from rest_framework import serializers

from measurements.models import Measurement
from users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    measurements = serializers.HyperlinkedRelatedField(
        queryset=Measurement.objects.all(),
        view_name='measurement-detail',
        many=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'measurements')


class MeasurementSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Measurement
        fields = ('user', 'date', 'height', 'weight')
