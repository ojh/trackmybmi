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
            is_accepted=False)

        return friendship


class Friendship(models.Model):
    """
    Representation of a relationship between two specific users.
    """
    PENDING = 'Pending'
    CONFIRMED = 'Confirmed'
    REJECTED = 'Rejected'
    ENDED = 'Ended'

    initiator = models.ForeignKey(User, related_name='outgoing_friendships',
                                  related_query_name='outgoing_friendship')
    recipient = models.ForeignKey(User, related_name='incoming_friendships',
                                  related_query_name='incoming_friendship')
    is_active = models.BooleanField(default=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return ('Friendship ({status}) between "{initiator}" and "{recipient}"'
                .format(status=self.get_status().lower(),
                        initiator=self.initiator.email,
                        recipient=self.recipient.email))

    @property
    def is_pending(self):
        return self.is_active and not self.is_accepted

    @property
    def is_confirmed(self):
        return self.is_active and self.is_accepted

    @property
    def is_rejected(self):
        return not self.is_active and not self.is_accepted

    @property
    def is_ended(self):
        return not self.is_active and self.is_accepted

    def get_status(self):
        if self.is_pending:
            status = self.PENDING

        elif self.is_confirmed:
            status = self.CONFIRMED

        elif self.is_rejected:
            status = self.REJECTED

        elif self.is_ended: # pragma: no branch
            status = self.ENDED

        return status
