from django.shortcuts import render

from rest_framework import permissions, viewsets

from .models import Measurement
from .serializers import MeasurementSerializer
from users.permissions import IsOwnerOrReadOnly


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
