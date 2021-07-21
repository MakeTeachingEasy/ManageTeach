import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

DAY_CHOICES= (
    ("M", "Monday"),
    ("Tu", "Tuesday"),
    ("Wed", "Wednesday"),
    ("Thu", "Thursday"),
    ("Fri", "Friday"),
    ("Sat", "Saturday"),
    ("Sun", "Sunday"),
)

TIME_CHOICES=(
    (datetime.time(14,0,0), "2PM"), 
    (datetime.time(15,0,0), "3PM"), 
    (datetime.time(16,0,0), "4PM"), 
    (datetime.time(17,0,0), "5PM"), 
    (datetime.time(18,0,0), "6PM"), 
)


# Create your models here.


class TutorSlot(models.Model):

    tutor= models.ForeignKey(User, on_delete=models.CASCADE, related_name="slots")
    day= models.CharField(max_length=20, choices=DAY_CHOICES)
    time= models.TimeField(choices=TIME_CHOICES)
    
    def __str__(self):
        return f"{self.tutor.first_name}: {self.day} at {self.time}"
    



    