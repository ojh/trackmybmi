from django.db import models
from custom_user.models import AbstractEmailUser


class User(AbstractEmailUser):
    """
    Extensible user model with email login.
    """

    def initiate_friendship(self, recipient):
        friendship = Friendship.objects.create(
            initiator=self,
            recipient=recipient,
            is_active=True,
            is_confirmed=False)

        return friendship


class Friendship(models.Model):
    """
    Representation of a relationship between two specific users.
    """
    initiator = models.ForeignKey(User, related_name='outgoing_friendships',
                                  related_query_name='outgoing_friendship')
    recipient = models.ForeignKey(User, related_name='incoming_friendships',
                                  related_query_name='incoming_friendship')
    is_active = models.BooleanField(default=True)
    is_confirmed = models.BooleanField(default=False)
