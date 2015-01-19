from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL

class Measurement(models.Model):
    """
    A record of a user's physical details at a particular point in time.
    """
    user = models.ForeignKey(User, related_name='measurements',
                                   related_query_name='measurement')

    date = models.DateField()

    height = models.DecimalField(max_digits=3, decimal_places=2,
                                 help_text="Height in metres")

    weight = models.DecimalField(max_digits=5, decimal_places=2,
                                 help_text="Mass in kilograms")

    class Meta:
        unique_together = (('user', 'date'),)

    def __str__(self):
        return "{} - {}".format(self.user.email, self.date.strftime('%Y-%m-%d'))

    def calculate_bmi(self):
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 1)
