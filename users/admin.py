from django.contrib import admin
from users.models import CustomUserModel
from django.contrib.auth.admin import UserAdmin
# Register your models here.
@admin.register(CustomUserModel)
class CustomUserModel(UserAdmin):
    model = CustomUserModel
    fieldsets = (
    (None, {
        'fields':(
            'username',
            'password'
        )
    }),

    ('Personal Info',{
        'fields':(
            'first_name',
            'last_name',
            'bio',
            'phone_number',
            'email',
            'profile_picture'
        )
    }),

    ('Permissions',{
        'fields':(
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions'
        )
    }),

    ('Important Dates',{
        'fields':('last_login',
        'date_joined'
        )
    })
    )

    add_fieldsets = (
        (None, {
            'classes' : ('wide'),
            'fields':('username', 'first_name', 'lastname', 'password1', 'password2', 'email', 'is_stuff')
        })
    )


    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('-username',)