from django.db import models
from custom_user.models import AbstractEmailUser


class User(AbstractEmailUser):
    """
    Extensible user model with email login.
    """
    pass
