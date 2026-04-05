from django.urls import path
from .views import PlaylistView, PingView, AnalyticsView

urlpatterns = [
    path('screens/playlist/', PlaylistView.as_view(), name='playlist'),
    path('screens/ping/', PingView.as_view(), name='ping'),
    path('screens/analytics/', AnalyticsView.as_view(), name='analytics'),
]
