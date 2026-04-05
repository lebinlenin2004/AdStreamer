from django.contrib import admin
from .models import Screen

@admin.register(Screen)
class ScreenAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'get_is_online', 'last_pinged')
    readonly_fields = ('pairing_token',)

    @admin.display(boolean=True, description='Online Status')
    def get_is_online(self, obj):
        return obj.is_online
