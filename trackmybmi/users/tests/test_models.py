from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
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
        self.assertEqual(friendship.status, friendship.PENDING)


class FriendshipTest(TestCase):
    def test_model_string(self):
        initiator = UserFactory(email='initiator@test.test')
        recipient = UserFactory(email='recipient@test.test')
        friendship = Friendship(initiator=initiator, recipient=recipient)

        model_string = ('Friendship (pending) between '
                        '"initiator@test.test" and "recipient@test.test"')

        self.assertEqual(friendship.__str__(), model_string)

    def test_new_friendship_not_saved_if_similar_one_already_exists(self):
        initiator = UserFactory()
        recipient = UserFactory()
        Friendship.objects.create(initiator=initiator, recipient=recipient)
        num_friendships = Friendship.objects.count()

        Friendship.objects.create(initiator=initiator, recipient=recipient)
        self.assertEqual(Friendship.objects.count(), num_friendships)

        Friendship.objects.create(initiator=recipient, recipient=initiator)
        self.assertEqual(Friendship.objects.count(), num_friendships)

        new_recipient = UserFactory()
        Friendship.objects.create(initiator=initiator, recipient=new_recipient)
        self.assertEqual(Friendship.objects.count(), num_friendships + 1)
