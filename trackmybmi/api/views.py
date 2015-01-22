from rest_framework import permissions, viewsets

from api.serializers import MeasurementSerializer, UserSerializer
from api.permissions import IsOwnerOrReadOnly
from measurements.models import Measurement
from users.models import User


class MeasurementViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents recorded measurements.

    The **user** of the measurement may update or delete instances
    of the measurement.
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """This endpoint presents the users in the system."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
