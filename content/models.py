from django.db import models
from accounts.models import User
from displays.models import Screen

class Ad(models.Model):
    title = models.CharField(max_length=255)
    advertiser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')
    media_file = models.FileField(upload_to='ads/')
    duration = models.PositiveIntegerField(default=10, help_text="Duration in seconds")
    is_active = models.BooleanField(default=True)
    approval_status = models.CharField(max_length=50, choices=(('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')), default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class AdAssignment(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='assignments')
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name='ad_assignments')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'start_date']

    def __str__(self):
        return f"{self.ad.title} on {self.screen.name}"
