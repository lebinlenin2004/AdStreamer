import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from content.models import AdAssignment
from django.utils import timezone

now = timezone.now()
with open("verify_debug.txt", "w", encoding="utf-8") as f:
    f.write(f"Current Time: {now}\n")
    f.write("-" * 40 + "\n")
    for a in AdAssignment.objects.all():
        ad = a.ad
        screen = a.screen
        is_active_now = a.start_date <= now <= a.end_date
        f.write(f"Assign ID: {a.id}\n")
        f.write(f"Screen: {screen.name} (Token: {screen.pairing_token})\n")
        f.write(f"Ad: {ad.title} (Status: {ad.approval_status}, Active: {ad.is_active})\n")
        f.write(f"Dates: {a.start_date} TO {a.end_date}\n")
        f.write(f"Is valid right now? {is_active_now and ad.is_active and ad.approval_status == 'APPROVED'}\n")
        f.write("\nDetails on why it might be invalid:\n")
        f.write(f"  Time check ({a.start_date} <= {now} <= {a.end_date}): {is_active_now}\n")
        f.write(f"  Ad is_active: {ad.is_active}\n")
        f.write(f"  Ad approval_status: {ad.approval_status}\n")
        f.write("-" * 40 + "\n")
