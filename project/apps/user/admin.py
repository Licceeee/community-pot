"""
Module: user admin

This module defines the admin for the user app.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, LastActive


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Admin for the CustomUser model."""

    search_fields = ("email", "first_name", "last_name")
    readonly_fields = ["last_login", "date_joined", "is_superuser"]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "email",
        "first_name",
        "last_name",
        "last_login",
        "get_groups",
        "is_staff",
        "is_superuser",
        "is_active",
    )
    list_filter = ("is_staff", "is_active", "id")
    # when edit existing user
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                    "is_superuser",
                    "date_joined",
                    "last_login",
                    "groups",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    # when adding a new user
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "date_joined",
                    "last_login",
                    "is_superuser",
                ),
            },
        ),
    )
    ordering = ("email",)


@admin.register(LastActive)
class LastActiveAdmin(admin.ModelAdmin):
    """Admin for the LastActive model."""

    list_filter = ("last_active",)
    search_fields = ("user__username",)
    list_display = ("user", "last_active")
    readonly_fields = ["last_active", "user"]
