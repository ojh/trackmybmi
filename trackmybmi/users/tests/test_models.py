from django.contrib.auth import get_user_model
from django.test import TestCase


User = get_user_model()

class UserTest(TestCase):
    def test_can_login_with_email(self):
        user = User.objects.create_user('test@test.test', 'testpassword')
        logged_in = self.client.login(username=user.email,
                                      password='testpassword')
        self.assertTrue(logged_in)
