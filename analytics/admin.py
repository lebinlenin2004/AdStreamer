import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import AdPlayLog

@admin.action(description='Download selected logs as CSV')
def download_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ad_play_logs.csv"'
    writer = csv.writer(response)
    writer.writerow(['Ad', 'Screen', 'Timestamp'])
    for log in queryset:
        writer.writerow([log.ad.title, log.screen.name, log.timestamp])
    return response

@admin.register(AdPlayLog)
class AdPlayLogAdmin(admin.ModelAdmin):
    list_display = ('ad', 'screen', 'timestamp')
    list_filter = ('screen', 'ad')
    search_fields = ('ad__title', 'screen__name')
    autocomplete_fields = ('ad',)
    readonly_fields = ('ad', 'screen', 'timestamp')
    search_form_template = 'admin/analytics/adplaylog/search_form.html'
    actions = [download_csv]
