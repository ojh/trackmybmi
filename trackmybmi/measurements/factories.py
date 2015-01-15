import factory
import datetime

from .models import Measurement
from users.factories import UserFactory


class MeasurementFactory(factory.django.DjangoModelFactory):
    """Create measurements with default attributes."""

    class Meta:
        model = Measurement

    user = factory.SubFactory(UserFactory)
    date = datetime.date.today()
