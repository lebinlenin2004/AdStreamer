from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from displays.models import Screen
from content.models import Ad, AdAssignment
from analytics.models import AdPlayLog
from django.db.models import Count
from django.utils import timezone
from .models import User
from .forms import CustomUserCreationForm, ScreenForm, AdApprovalForm, AdAssignmentForm, AdUploadForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def admin_dashboard(request):
    if request.user.role != 'ADMIN':
        return redirect('dashboard')
    
    screens = Screen.objects.all()
    ads = Ad.objects.all()
    logs_count = AdPlayLog.objects.count()
    
    now = timezone.now()
    active_assignments = AdAssignment.objects.filter(
        start_date__lte=now,
        end_date__gte=now,
        ad__is_active=True,
        ad__approval_status='APPROVED'
    ).select_related('screen', 'ad')
    
    context = {
        'screens': screens,
        'ads': ads,
        'logs_count': logs_count,
        'active_assignments': active_assignments,
    }
    return render(request, 'accounts/admin_dashboard.html', context)

@login_required
def advertiser_dashboard(request):
    if request.user.role != 'ADVERTISER':
        return redirect('dashboard')
        
    my_ads = Ad.objects.filter(advertiser=request.user).order_by('-created_at')
    my_logs_count = AdPlayLog.objects.filter(ad__advertiser=request.user).count()
    
    if request.method == 'POST':
        upload_form = AdUploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            new_ad = upload_form.save(commit=False)
            new_ad.advertiser = request.user
            new_ad.save()
            return redirect('advertiser_dashboard')
    else:
        upload_form = AdUploadForm()
    
    context = {
        'my_ads': my_ads,
        'my_logs_count': my_logs_count,
        'upload_form': upload_form,
    }
    return render(request, 'accounts/advertiser_dashboard.html', context)

@login_required
def admin_users(request):
    if request.user.role != 'ADMIN':
        return redirect('dashboard')
    users = User.objects.all().order_by('-date_joined')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_users')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/admin_users.html', {'users': users, 'form': form})

@login_required
def admin_screens(request):
    if request.user.role != 'ADMIN':
        return redirect('dashboard')
    screens = Screen.objects.all().order_by('-name')
    if request.method == 'POST':
        form = ScreenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_screens')
    else:
        form = ScreenForm()
    return render(request, 'accounts/admin_screens.html', {'screens': screens, 'form': form})

@login_required
def admin_ads(request):
    if request.user.role != 'ADMIN':
        return redirect('dashboard')
    ads = Ad.objects.all().order_by('-created_at')
    
    if request.method == 'POST':
        if 'ad_id' in request.POST:
            ad_obj = Ad.objects.get(id=request.POST.get('ad_id'))
            form = AdApprovalForm(request.POST, instance=ad_obj)
            if form.is_valid():
                form.save()
                return redirect('admin_ads')
        else:
            upload_form = AdUploadForm(request.POST, request.FILES)
            if upload_form.is_valid():
                new_ad = upload_form.save(commit=False)
                new_ad.advertiser = request.user
                new_ad.approval_status = 'APPROVED' # Admins auto-approve their own uploads
                new_ad.save()
                return redirect('admin_ads')
                
    upload_form = AdUploadForm()
    return render(request, 'accounts/admin_ads.html', {'ads': ads, 'upload_form': upload_form})

@login_required
def admin_assignments(request):
    if request.user.role != 'ADMIN':
        return redirect('dashboard')
    assignments = AdAssignment.objects.all().order_by('screen', 'display_order')
    if request.method == 'POST':
        form = AdAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_assignments')
    else:
        form = AdAssignmentForm()
    return render(request, 'accounts/admin_assignments.html', {'assignments': assignments, 'form': form})

@login_required
def admin_system_logs(request):
    if request.user.role != 'ADMIN':
        return redirect('dashboard')
    # Render the initial page, the javascript will fetch logs
    return render(request, 'accounts/admin_system_logs.html')

@login_required
def admin_system_logs_api(request):
    if request.user.role != 'ADMIN':
        return JsonResponse({'error': 'Unauthorized'}, status=403)
        
    # Get recent logs
    logs = AdPlayLog.objects.select_related('ad', 'screen').order_by('-timestamp')[:50]
    
    data = []
    for log in logs:
        # Format the time nicely for the terminal look
        # Since TIME_ZONE is Asia/Kolkata, Django handles timezone-aware datetime natively when using local time if configured.
        # But we'll format it right here to guarantee string format.
        local_time = timezone.localtime(log.timestamp)
        data.append({
            'id': log.id,
            'time': local_time.strftime('%Y-%m-%d %H:%M:%S'),
            'screen_name': log.screen.name,
            'ad_title': log.ad.title,
            'advertiser': log.ad.advertiser.username,
        })
        
    return JsonResponse({'logs': data})
