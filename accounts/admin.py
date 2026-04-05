from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Roles', {'fields': ('role',)}),
    )
    list_display = UserAdmin.list_display + ('role',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
