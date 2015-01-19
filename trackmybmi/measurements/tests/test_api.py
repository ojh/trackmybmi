from django.test import TestCase


class MeasurementAPITest(TestCase):
    def test_list_measurements_url(self):
        response = self.client.get('/api/measurements/')
        self.assertEqual(response.status_code, 200)
