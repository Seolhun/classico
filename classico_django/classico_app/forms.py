from django import forms
from django.contrib.auth.models import User
from classico_app.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }


class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('profile_site', 'profile_pics')
