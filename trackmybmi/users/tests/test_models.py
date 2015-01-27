from django.contrib.auth import get_user_model
from django.test import TestCase

from users.factories import UserFactory


User = get_user_model()

class UserTest(TestCase):
    def test_can_login_with_email(self):
        user = User.objects.create_user('test@test.test', 'testpassword')
        logged_in = self.client.login(username=user.email,
                                      password='testpassword')
        self.assertTrue(logged_in)

    def test_user_can_initiate_friendship(self):
        initiator = UserFactory()
        recipient = UserFactory()
        friendship = initiator.initiate_friendship(recipient)
        self.assertEqual(friendship.initiator, initiator)
        self.assertEqual(friendship.recipient, recipient)
        self.assertTrue(friendship.is_active)
        self.assertFalse(friendship.is_confirmed)
