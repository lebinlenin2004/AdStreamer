from django.db import models
from content.models import Ad
from displays.models import Screen

class AdPlayLog(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='play_logs')
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name='play_logs')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ad.title} played on {self.screen.name} at {self.timestamp}"
