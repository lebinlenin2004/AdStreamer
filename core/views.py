from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    if request.user.role == 'ADMIN':
        return redirect('admin_dashboard')
    return redirect('advertiser_dashboard')
