from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from django.utils.translation import gettext_lazy as _


class UsersInline(admin.TabularInline):
    model = UserProfile
    fields = ('username', 'role')
    extra = 0


class UserProfileAdmin(UserAdmin):
    fieldsets = (
        (None,
            {'fields': ('username', 'password')}),
        (_('Personal info'),
            {'fields':
                ('first_name',
                 'last_name',
                 'email',
                 'company',
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
