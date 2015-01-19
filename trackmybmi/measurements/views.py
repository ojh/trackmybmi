from django.shortcuts import render

from rest_framework import viewsets

from .models import Measurement
from .serializers import MeasurementSerializer


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
