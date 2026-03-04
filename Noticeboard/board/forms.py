from django import forms
from .models import Notice
from django.contrib.auth.models import User
from .models import Profile

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter text', 'rows': 3}),
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter new username'
            }),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write something about yourself'
            }),
        }