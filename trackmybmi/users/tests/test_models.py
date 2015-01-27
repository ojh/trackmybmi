from django.contrib.auth import get_user_model
from django.test import TestCase

from users.factories import FriendshipFactory, UserFactory
from users.models import Friendship


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
        self.assertFalse(friendship.is_accepted)


class FriendshipTest(TestCase):
    def test_model_string(self):
        initiator = UserFactory(email='initiator@test.test')
        recipient = UserFactory(email='recipient@test.test')
        friendship = Friendship(initiator=initiator, recipient=recipient)

        model_string = ('Friendship (pending) between '
                        '"initiator@test.test" and "recipient@test.test"')

        self.assertEqual(friendship.__str__(), model_string)

    def test_get_friendship_status(self):
        pending = FriendshipFactory(is_accepted=False, is_active=True)
        self.assertTrue(pending.is_pending)
        self.assertFalse(pending.is_confirmed)
        self.assertFalse(pending.is_rejected)
        self.assertFalse(pending.is_ended)
        self.assertEqual(pending.get_status(), Friendship.PENDING)

        confirmed = FriendshipFactory(is_accepted=True, is_active=True)
        self.assertFalse(confirmed.is_pending)
        self.assertTrue(confirmed.is_confirmed)
        self.assertFalse(confirmed.is_rejected)
        self.assertFalse(confirmed.is_ended)
        self.assertEqual(confirmed.get_status(), Friendship.CONFIRMED)

        rejected = FriendshipFactory(is_accepted=False, is_active=False)
        self.assertFalse(rejected.is_pending)
        self.assertFalse(rejected.is_confirmed)
        self.assertTrue(rejected.is_rejected)
        self.assertFalse(rejected.is_ended)
        self.assertEqual(rejected.get_status(), Friendship.REJECTED)

        ended = FriendshipFactory(is_accepted=True, is_active=False)
        self.assertFalse(ended.is_pending)
        self.assertFalse(ended.is_confirmed)
        self.assertFalse(ended.is_rejected)
        self.assertTrue(ended.is_ended)
        self.assertEqual(ended.get_status(), Friendship.ENDED)
