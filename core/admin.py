from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import User

class CustomUserAdmin(UserAdmin):
    # Adding fields to the existing fieldsets for the user detail page
    fieldsets = UserAdmin.fieldsets + (
        (
            "Other Fields",  # Section title
            {
                "fields": (
                    
                    'user_type',
                    
                )
            },
        ),
    )

    # Adding fields to the existing add_fieldsets for the user creation page
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Other Fields",  # Section title for user creation form
            {
                "fields": (
                    'first_name',
                    'last_name',
                    'email',
                    'password',
                    'user_type',
                    
                )
            },
        ),
    )

admin.site.register(User, CustomUserAdmin)
