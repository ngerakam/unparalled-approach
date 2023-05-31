from django.contrib import admin

from .models import User, UserProfile


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = [
        "username",
        "email",
        "is_staff",
        "is_superuser",
    ]
    search_fields = [
        "username__istartswith",
        "email__istartswith",
    ]
    list_filter = [
        "is_staff",
        "is_superuser",
    ]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        "user_name",
        "email",
        "phone_number",
        "birth_date",
    ]
    autocomplete_fields = [
        "user",
    ]

    def user_name(self, userprofile):
        return userprofile.user.username

    def email(self, userprofile):
        return userprofile.user.email

    def phone_number(self, userprofile):
        return userprofile.phone_no
