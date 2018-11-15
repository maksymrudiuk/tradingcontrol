from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from django.utils.translation import gettext_lazy as _


class UserProfileAdmin(UserAdmin):
    fieldsets = (
        (None,
            {'fields': ('username', 'password')}),
        (_('Personal info'),
            {'fields':
                ('first_name',
                 'last_name',
                 'email',
                 'role',
                 'phone',
                 'user_photo')}),
        (_('Permissions'),
            {'fields':
                ('is_active',
                 'is_staff',
                 'is_superuser',
                 'groups',
                 'user_permissions',
                 )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(UserProfile, UserProfileAdmin)
