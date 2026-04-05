from django.contrib import admin
from .models import AdPlayLog

@admin.register(AdPlayLog)
class AdPlayLogAdmin(admin.ModelAdmin):
    list_display = ('ad', 'screen', 'timestamp')
    list_filter = ('screen', 'ad')
    readonly_fields = ('ad', 'screen', 'timestamp')
