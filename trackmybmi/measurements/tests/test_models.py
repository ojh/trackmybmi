import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from measurements.factories import MeasurementFactory
from measurements.models import Measurement
from users.factories import UserFactory


class MeasurementTest(TestCase):
    def test_string_method(self):
        user = UserFactory(email='test@test.test')
        date = datetime.date(2015, 1, 1)
        measurement = MeasurementFactory(user=user, date=date)
        self.assertEqual(measurement.__str__(), "test@test.test - 2015-01-01")

    def test_users_can_only_have_one_measurement_per_date(self):
        user = UserFactory(email='test@test.test')
        date = datetime.date(2015, 1, 1)
        measurement = MeasurementFactory(user=user, date=date)
        with self.assertRaises(ValidationError):
            same_user_same_day = MeasurementFactory(user=user, date=date)
            same_user_same_day.full_clean()

    def test_calculate_bmi(self):
        measurement = MeasurementFactory(height=1.74, weight=65.0)
        self.assertEqual(measurement.calculate_bmi(), 21.5)
