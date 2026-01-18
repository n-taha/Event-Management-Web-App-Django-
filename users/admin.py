from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUserModel


@admin.register(CustomUserModel)
class CustomUserAdmin(UserAdmin):
    model = CustomUserModel

    fieldsets = (
        (None, {
            'fields': ('username', 'password'),
        }),
        ('Personal Info', {
            'fields': (
                'first_name',
                'last_name',
                'bio',
                'phone_number',
                'email',
                'profile_picture',
            ),
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined'),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'first_name',
                'last_name',
                'email',
                'password1',
                'password2',
                'is_staff',
            ),
        }),
    )

    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('-username',)
