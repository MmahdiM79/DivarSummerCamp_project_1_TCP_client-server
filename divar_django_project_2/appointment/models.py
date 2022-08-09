import django.contrib.auth.models
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserBioGender(AbstractUser):
    
    class Gender(models.TextChoices):
        MALE = 'male', _('مرد')
        FEMALE = 'female', _('زن')
        
    bio = models.CharField(max_length=256, null=True, blank=True)
    pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    gender = models.CharField(choices=Gender.choices, max_length=10, null=True, blank=True)
    
    