import datetime

from django.core.urlresolvers import reverse
from rest_framework import serializers, status
from rest_framework.test import APITestCase

from measurements.factories import MeasurementFactory
from users.factories import UserFactory


class MeasurementAPITest(APITestCase):
    def setUp(self):
        self.user = UserFactory(email='user@test.test')
        self.measurement = MeasurementFactory(
            user=self.user,
            height=1.74,
            weight=75.00,
            date=datetime.date(2015, 1, 19))


    def test_must_be_logged_in_to_create_new_measurement(self):
        data = {
            'date': '2015-01-18',
            'height': 1.74,
            'weight': 78.00,
        }

        url = reverse('measurement-list')

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data['user'], self.user.email)


    def test_measurement_date_and_user_are_unique_together(self):
        data = {
            'date': '2015-01-19',
            'height': 1.74,
            'weight': 75.00,
        }

        url = reverse('measurement-list')

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        error_msg = ("Users may only log a single measurement "
                     "against any given date.")

        self.assertIn(error_msg, response.data['non_field_errors'])


    def test_list_measurements(self):
        # TODO: Rename to `test_must_be_logged_in_to_list_own_measurements`...
        #       ... and modify code accordingly.

        response = self.client.get(reverse('measurement-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 1)
        measurement = response.data[0]
        self.assertIn('id', measurement)
        self.assertEqual(measurement['user'], 'user@test.test')
        self.assertEqual(measurement['date'], '2015-01-19')
        self.assertEqual(measurement['height'], '1.74')
        self.assertEqual(measurement['weight'], '75.00')


    #~ def test_must_be_logged_in_and_be_friends_to_list_someone_elses_measurements(self):
        #~ pass


    def test_get_measurement_detail(self):
        # TODO: Rename to `test_must_be_logged_in_to_get_own_measurement_detail`...
        #       ... and modify code accordingly.

        url = reverse('measurement-detail', args=[self.measurement.id])
        response = self.client.get(url, format='json')

        measurement = response.data
        self.assertIn('id', measurement)
        self.assertEqual(measurement['user'], 'user@test.test')
        self.assertEqual(measurement['date'], '2015-01-19')
        self.assertEqual(measurement['height'], '1.74')
        self.assertEqual(measurement['weight'], '75.00')


    #~ def test_must_be_logged_in_and_be_friends_to_get_someone_elses_measurement_detail(self):
        #~ pass


    def test_must_be_logged_in_to_edit_own_measurement(self):
        url = reverse('measurement-detail', args=[self.measurement.id])

        data = {'weight': 75.01}

        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['weight'], '75.01')


    def test_cannot_edit_someone_elses_measurement(self):
        other_user = UserFactory(email='other.user@test.test')
        not_my_measurement = MeasurementFactory(
            user=other_user,
            height=1.63,
            weight=55.00,
            date=datetime.date(2015, 1, 19))

        data = {'weight': 55.01}

        self.client.force_authenticate(user=self.user)

        url = reverse('measurement-detail', args=[not_my_measurement.id])
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    #~ def test_cannot_edit_measurements_of_friends(self):
        #~ pass


    #~ def test_date_field_is_not_editable(self):
        #~ """
        #~ Date fields are read-only; to change date, a new measurement
        #~ must be created (or an existing one updated).
        #~ """
        #~ pass


    def test_must_be_logged_in_to_delete_own_measurement(self):
        url = reverse('measurement-detail', args=[self.measurement.id])

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_cannot_delete_someone_elses_measurement(self):
        other_user = UserFactory(email='other.user@test.test')
        not_my_measurement = MeasurementFactory(
            user=other_user,
            height=1.63,
            weight=55.00,
            date=datetime.date(2015, 1, 19))

        self.client.force_authenticate(user=self.user)

        url = reverse('measurement-detail', args=[not_my_measurement.id])
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    #~ def test_cannot_delete_measurements_of_friends(self):
        #~ pass
