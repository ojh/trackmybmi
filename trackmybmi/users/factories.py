import factory

from django.contrib.auth.hashers import make_password

from .models import Friendship, User


class UserFactory(factory.django.DjangoModelFactory):
    """Create users with default attributes."""

    class Meta:
        model = User

    email = factory.Sequence(lambda n: 'user.{}@test.test'.format(n))
    password = make_password('password')


class FriendshipFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Friendship

    initiator = factory.SubFactory(UserFactory)
    recipient = factory.SubFactory(UserFactory)
