from rest_framework import serializers
from content.models import Ad, AdAssignment
from displays.models import Screen
from analytics.models import AdPlayLog

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'title', 'media_file', 'duration']
