from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from displays.models import Screen
from content.models import AdAssignment
from analytics.models import AdPlayLog
from .serializers import AdSerializer

from django.core.exceptions import ValidationError

class ScreenAuthMixin:
    authentication_classes = []
    permission_classes = []

    def get_screen(self, request):
        token = request.GET.get('token') or request.data.get('token')
        if not token:
            return None
        token = token.replace('<', '').replace('>', '')
        try:
            return Screen.objects.get(pairing_token=token)
        except (Screen.DoesNotExist, ValidationError, ValueError):
            return None

class PlaylistView(ScreenAuthMixin, APIView):
    def get(self, request):
        screen = self.get_screen(request)
        if not screen:
            return Response({"error": "Invalid or missing token"}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Update last pinged
        screen.last_pinged = timezone.now()
        screen.save()

        # Get active assignments
        now = timezone.now()
        assignments = AdAssignment.objects.filter(
            screen=screen,
            start_date__lte=now,
            end_date__gte=now,
            ad__is_active=True,
            ad__approval_status='APPROVED'
        ).select_related('ad')

        ads = [assignment.ad for assignment in assignments]
        serializer = AdSerializer(ads, many=True)
        return Response({"playlist": serializer.data})

class PingView(ScreenAuthMixin, APIView):
    def post(self, request):
        screen = self.get_screen(request)
        if not screen:
            return Response({"error": "Invalid or missing token"}, status=status.HTTP_401_UNAUTHORIZED)
        
        screen.last_pinged = timezone.now()
        screen.save()
        return Response({"status": "ok"})

class AnalyticsView(ScreenAuthMixin, APIView):
    def post(self, request):
        screen = self.get_screen(request)
        if not screen:
            return Response({"error": "Invalid or missing token"}, status=status.HTTP_401_UNAUTHORIZED)
        
        ad_id = request.data.get('ad_id')
        if not ad_id:
            return Response({"error": "Missing ad_id"}, status=status.HTTP_400_BAD_REQUEST)
            
        AdPlayLog.objects.create(ad_id=ad_id, screen=screen)
        return Response({"status": "logged"})
