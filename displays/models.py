from django.db import models
import uuid

class Screen(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    pairing_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status = models.CharField(max_length=20, choices=(('ONLINE', 'Online'), ('OFFLINE', 'Offline')), default='OFFLINE')
    last_pinged = models.DateTimeField(null=True, blank=True)

    @property
    def is_online(self):
        from django.utils import timezone
        import datetime
        if not self.last_pinged:
            return False
        return timezone.now() - self.last_pinged < datetime.timedelta(minutes=2)

    def __str__(self):
        return f"{self.name} - {self.location}"
