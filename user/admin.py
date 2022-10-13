from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Additional Info',
            {
                'fields': (
                    'role',
                )
            }
        )
    )


admin.site.register(CustomUser, CustomUserAdmin)
