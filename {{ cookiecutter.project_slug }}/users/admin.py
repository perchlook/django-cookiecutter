from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DJUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


class UserAdmin(DJUserAdmin):
    list_display = (
        'email',
        'first_name',
        'is_staff',
        'is_superuser',
    )


admin.site.register(User, UserAdmin)
