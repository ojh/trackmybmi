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
    user = serializers.CharField(
        read_only=True,
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Measurement
        fields = ('id', 'user', 'date', 'height', 'weight')

        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Measurement.objects.all(),
                fields=('user', 'date'),
                message=("Users may only log a single measurement "
                         "against any given date.")
            )
        ]
