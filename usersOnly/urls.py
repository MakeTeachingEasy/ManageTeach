from django.urls import path
from .views import *
urlpatterns=[
    path("log/", attendenceView),
    path("tutor-log/", myLogView),
    path("modify-schedule", modifyScheduleView),
    path("my-slots", mySlotsView),
    path("tutor-slots", tutorSlotsView),
]
