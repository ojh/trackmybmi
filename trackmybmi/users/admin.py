from django.contrib import admin
from custom_user.admin import EmailUserAdmin
from .models import User


class UserAdmin(EmailUserAdmin):
    """
    Extensible admin interface for custom user model.
    """
    pass


admin.site.register(User, UserAdmin)
