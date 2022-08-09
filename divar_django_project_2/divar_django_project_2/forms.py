from django import forms
from django.core import validators



class ContactUsForm(forms.Form):
    title = forms.CharField(max_length=128, label='موضوع', required=True)
    email = forms.EmailField(label='ایمیل', required=True)
    message = forms.CharField(widget=forms.Textarea, label='پیام',
                              validators=[validators.MinLengthValidator(10), 
                                          validators.MaxLengthValidator(250)])