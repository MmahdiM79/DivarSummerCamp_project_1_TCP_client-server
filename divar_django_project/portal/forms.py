from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from .models import Course
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
    
    class Meta:
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        model = User
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل',
            'username': 'نام کاربری',
            'password1': 'گذرواژه',
            'password2': 'تکرار گذرواژه',
        }
        error_messages = {
            'username': {
                'unique': 'نام کاربری تکراری است',
            },
            'password1': {
                'same': 'گذرواژه و تکرار گذرواژه باید یکسان باشد',
            },
            'email': {
                'unique': 'ایمیل تکراری است',
            }
        }
        
        
class LoginForm(AuthenticationForm):
    class Meta:
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': 'نام کاربری',
            'password': 'گذرواژه',
        }
        error_messages = {
            'username': {
                'invalid': 'نام کاربری صحیح نیست',
            },
            'password': {
                'invalid': 'گذرواژه صحیح نیست',
            },
        }
        

class EditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
        }
        
    def clean(self):
        super().clean()
        self.cleaned_data.pop('first_name') if self.cleaned_data.get('last_name') == '' else None
        self.cleaned_data.pop('last_name') if self.cleaned_data.get('first_name') == '' else None
        
        return self.cleaned_data


class NewCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
