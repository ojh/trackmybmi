import datetime

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase

from measurements.factories import MeasurementFactory
from users.factories import UserFactory


class MeasurementAPITest(APITestCase):
    def test_list_measurements(self):
        email = 'test@test.test'
        user = UserFactory(email=email)

        measurement = MeasurementFactory(user=user, height=1.74, weight=75.00,
                                         date=datetime.date(2015, 1, 19))

        response = self.client.get(reverse('measurement-list'), format='json')
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data, [{
            'user': email,
            'date': '2015-01-19',
            'height': '1.74',
            'weight': '75.00',
        }])

    def test_must_be_logged_in_to_post_new_measurement(self):
        user = UserFactory()

        data = {
            'date': '2015-01-19',
            'height': '1.74',
            'weight': '78.00',
        }

        url = reverse('measurement-list')

        # Try to post data without being authenticated:
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 403)

        # Try again, this time whilst authenticated:
        self.client.force_authenticate(user=user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
