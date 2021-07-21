from django.contrib import admin
from .models import AbsenceType, Log, Student, Grade, Board
from usersOnly.models import TutorSlot
# Register your models here.

admin.site.register(Grade)
admin.site.register(Student)
admin.site.register(Board)
admin.site.register(Log)
admin.site.register(AbsenceType)
admin.site.register(TutorSlot)