import factory

from django.contrib.auth.hashers import make_password

from .models import User


class UserFactory(factory.django.DjangoModelFactory):
    """Create users with default attributes."""

    class Meta:
        model = User

    email = factory.Sequence(lambda n: 'user.{}@test.test'.format(n))
    password = make_password('password')
