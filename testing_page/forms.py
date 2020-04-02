from django import forms
from user.models import User


class UpdateStatus(forms.ModelForm):
    """Form for update user status"""
    class Meta:
        model = User
        fields = ('status',)
