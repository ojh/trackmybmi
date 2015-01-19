from django.test import TestCase

class MeasurementAdminURLTest(TestCase):
    def test_list_admin_url(self):
        response = self.client.get('/admin/measurements/', follow=True)
        self.assertEqual(response.status_code, 200)
