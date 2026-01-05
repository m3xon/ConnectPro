from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'about', 'skills', 'experience', 'full_name', 'major', 'address']
        widgets = {
            'about': forms.Textarea(attrs={'class': 'input-textarea'}),
            'skills': forms.Textarea(attrs={'class': 'input-textarea'}),
            'experience': forms.Textarea(attrs={'class': 'input-textarea'}),
            'full_name': forms.TextInput(attrs={'class': 'input-text'}),
            'major': forms.TextInput(attrs={'class': 'input-text'}),
            'address': forms.TextInput(attrs={'class': 'input-text'}),
        }
