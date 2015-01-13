from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.test import TestCase


User = get_user_model()

class UserTest(TestCase):
    def test_can_login_with_email(self):
        password = make_password('testpassword')
        user = User.objects.create(email='test@test.test', password=password)
        logged_in = self.client.login(username=user.email, password='testpassword')
        self.assertTrue(logged_in)
