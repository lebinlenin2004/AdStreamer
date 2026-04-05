from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from displays.models import Screen
from content.models import Ad, AdAssignment

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('role',)

class ScreenForm(forms.ModelForm):
    class Meta:
        model = Screen
        fields = ['name', 'location']

class AdUploadForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'media_file', 'duration']

class AdApprovalForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['approval_status', 'is_active']

class AdAssignmentForm(forms.ModelForm):
    class Meta:
        model = AdAssignment
        fields = ['ad', 'screen', 'start_date', 'end_date', 'display_order']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
