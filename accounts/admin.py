from django.contrib import admin

from .models import User, Profile


class ProfileInline(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
        'is_superuser'
    )
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    inlines = (ProfileInline, )
