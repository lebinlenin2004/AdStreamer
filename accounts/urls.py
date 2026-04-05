from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/advertiser/', views.advertiser_dashboard, name='advertiser_dashboard'),
    path('dashboard/admin/users/', views.admin_users, name='admin_users'),
    path('dashboard/admin/screens/', views.admin_screens, name='admin_screens'),
    path('dashboard/admin/ads/', views.admin_ads, name='admin_ads'),
    path('dashboard/admin/assignments/', views.admin_assignments, name='admin_assignments'),
    path('dashboard/admin/logs/', views.admin_system_logs, name='admin_system_logs'),
    path('dashboard/admin/logs/api/', views.admin_system_logs_api, name='admin_system_logs_api'),
]
