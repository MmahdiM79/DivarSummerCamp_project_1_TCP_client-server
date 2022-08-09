from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Course(models.Model):
    class DaysOfWeek(models.IntegerChoices):
        SAT = 0, _('شنبه')
        SUN = 1, _('یکشنبه')
        MON = 2, _('دوشنبه')
        TUE = 3, _('سه شنبه')
        THU = 4, _('چهارشنبه')
        
        
    name = models.CharField(max_length=128, blank=False, null=False)
    code = models.CharField(max_length=128, blank=False, null=False)
    group = models.IntegerField(blank=False, null=False)
    
    department = models.CharField(max_length=128, blank=False, null=False)
    professor = models.CharField(max_length=128, blank=False, null=False)
    
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    first_day = models.IntegerField(choices=DaysOfWeek.choices, blank=False, null=False)
    second_day = models.IntegerField(choices=DaysOfWeek.choices, blank=True, null=True)
    
    
    
    
