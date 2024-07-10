from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


class CustomUserAdmin(UserAdmin):
    model = models.User
    list_display = ["username", "email"]
    fieldsets = [
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined", "img", "bio")}),
    ]


admin.site.register(models.User, CustomUserAdmin)
admin.site.register(models.Blog)
admin.site.register(models.BlogImg)
admin.site.register(models.BlogVideo)
admin.site.register(models.Comment)
