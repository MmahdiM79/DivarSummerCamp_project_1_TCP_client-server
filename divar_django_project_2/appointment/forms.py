from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from .models import UserBioGender

from django.contrib.auth.models import Group
professors, _ = Group.objects.get_or_create(name='Professor')
students, _ = Group.objects.get_or_create(name='Student')



class RegisterForm(UserCreationForm):
    account_type = forms.ChoiceField(choices=((professors.id, 'Professor'), (students.id, 'Student')))
    
    class Meta:
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        model = UserBioGender
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


class EditForm(forms.ModelForm):
    class Meta:
        model = UserBioGender
        fields = ('first_name', 'last_name', 'gender', 'bio', 'pic')
        
        
    def clean(self):
        super().clean()
        self.cleaned_data.pop('first_name') if self.cleaned_data.get('last_name') == '' else None
        self.cleaned_data.pop('last_name') if self.cleaned_data.get('first_name') == '' else None
        # self.cleaned_data.pop('bio') if self.cleaned_data.get('bio') == '' else None
        # self.cleaned_data.pop('pic') if self.cleaned_data.get('pic') == '' else None
        # self.cleaned_data.pop('gender') if self.cleaned_data.get('gender') == '' else None
        
        return self.cleaned_data
