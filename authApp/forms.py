from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class SignUp(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Password"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password',]

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('confirm_password'):
            raise forms.ValidationError("Password does not match")
        return cleaned_data          
    
    
class Login(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Password"
    ) 