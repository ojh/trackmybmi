from django.test import TestCase

from measurements.factories import MeasurementFactory
from measurements.models import Measurement


class MeasurementTest(TestCase):
    def test_calculate_bmi(self):
        measurement = MeasurementFactory(height=1.74, weight=65.0)
        self.assertEqual(measurement.calculate_bmi(), 21.5)
