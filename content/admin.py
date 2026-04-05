from django.contrib import admin
from .models import Ad, AdAssignment

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'advertiser', 'duration', 'is_active', 'approval_status')
    list_filter = ('is_active', 'approval_status')

@admin.register(AdAssignment)
class AdAssignmentAdmin(admin.ModelAdmin):
    list_display = ('ad', 'screen', 'start_date', 'end_date', 'display_order')
    list_filter = ('screen',)
