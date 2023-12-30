from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdmin_
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin_):
    fieldsets = (
        (None, {"fields": ("username", "password", "profile_image", "friends")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_filter = ('gender', 'created_at')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
