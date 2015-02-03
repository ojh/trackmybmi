from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from custom_user.models import AbstractEmailUser


class User(AbstractEmailUser):
    """
    Extensible user model with email login.
    """

    def initiate_friendship(self, recipient):
        friendship = Friendship.objects.create(
            initiator=self,
            recipient=recipient)

        return friendship


class Friendship(models.Model):
    """
    Representation of a relationship between two specific users.
    """
    PENDING = 'PENDING'
    ACTIVE = 'ACTIVE'
    REJECTED = 'REJECTED'
    ENDED = 'ENDED'

    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (ACTIVE, 'Active'),
        (REJECTED, 'Rejected'),
        (ENDED, 'Ended'),
    )

    initiator = models.ForeignKey(User, related_name='outgoing_friendships',
                                  related_query_name='outgoing_friendship')
    recipient = models.ForeignKey(User, related_name='incoming_friendships',
                                  related_query_name='incoming_friendship')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES,
                              default=PENDING, editable=False)

    class Meta:
        unique_together = (('initiator', 'recipient'),)

    def __str__(self):
        return ('Friendship ({status}) between "{initiator}" and "{recipient}"'
                .format(status=self.get_status_display().lower(),
                        initiator=self.initiator.email,
                        recipient=self.recipient.email))

    def save(self, *args, **kwargs):
        similar_friendships = Friendship.objects.filter(
            (Q(initiator=self.initiator) & Q(recipient=self.recipient)) |
            (Q(initiator=self.recipient) & Q(recipient=self.initiator))
        ).exclude(pk=self.pk).count()

        if not similar_friendships:
            super().save(*args, **kwargs)
