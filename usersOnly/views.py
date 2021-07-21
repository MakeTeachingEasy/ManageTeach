from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
import datetime
from main.models import Student, Log, Grade, AbsenceType
from usersOnly.models import TutorSlot, DAY_CHOICES, TIME_CHOICES
from django.contrib.auth.models import User
# Create your views here.

def attendenceView(response):
    students_class_wise= {}
    for i in range(6,12):
        students_class_wise[i]=(Student.objects.filter(grade=Grade.objects.get(grade=i)).order_by("f_name"))
    if not response.user.is_authenticated:
        return redirect("/login")

    if response.method=='POST':
        if (not int(response.POST.get("time")) in range(2,7)) or \
             (not response.POST.get("date")):
            return render(response, "usersOnly/attendence.html", {
                "user": response.user, 
                "students_class_wise": students_class_wise,
                "illegal_entry": True,
            })
            
        else:
            print(response.POST)
            date= response.POST.get("date")
            time= datetime.time(int(response.POST.get("time"))+12, 0, 0)
            log_array=[]
            for student in Student.objects.all():
                if response.POST.get(f"c{student.id}") == "present":
                    log= Log()
                    log.logIt(response.user, student, date, time, True, AbsenceType.objects.get(type="Does Not Apply"))
                    log.save()
                    log_array.append(log)
                elif response.POST.get(f"c{student.id}") == "informed":
                    log= Log()
                    log.logIt(response.user, student, date, time, False, AbsenceType.objects.get(type="Informed"))
                    log.save()
                    log_array.append(log)
                elif response.POST.get(f"c{student.id}") == "uninformed":
                    log=Log()
                    log.logIt(response.user, student, date, time, False, AbsenceType.objects.get(type="Uninformed"))
                    log.save()
                    log_array.append(log)
            return myLogView(response, True, log_array)
            
    return render(response, "usersOnly/attendence.html", {
        "user": response.user, 
        "students_class_wise": students_class_wise,
        "illegal_entry": False,
        })
def myLogView(response, submitted=False, log_array=[]):
    if response.user.is_authenticated:
        all_logs= Log.objects.filter(tutor=response.user)
        return render(response, "usersOnly/myLogs.html", {
            "logs": all_logs.order_by("date").reverse(),
            "submitted": submitted,
            "log_array": log_array,
        })
    else:
        return redirect('/login')

def modifyScheduleView(response):
    if not response.user.is_authenticated:
        return redirect("/login")

    if response.method=="POST":
        TutorSlot.objects.filter(tutor=response.user).delete()
        for day_code, day in DAY_CHOICES:
            for time, time_string in TIME_CHOICES:
                if response.POST.get(f"{day_code}{time_string}"):
                    slot= TutorSlot(tutor= response.user, day=day_code, time=time)
                    slot.save()
        return redirect("/user/my-slots")
    return render(response, "usersOnly/modifySchedule.html", {
        "user": response.user,
        "days": DAY_CHOICES,
        "times": TIME_CHOICES,
    })

def mySlotsView(response):
    if not response.user.is_authenticated:
        return redirect("/login")
    tutor_slots= TutorSlot.objects.filter(tutor= response.user).order_by("time")
    return render(response, "usersOnly/mySlots.html", {
        "user": response.user,
        "slots" : tutor_slots,
        "days": DAY_CHOICES,
    })

def tutorSlotsView(response):
    print(datetime.date.today().strftime('%A'))
    return render(response, "usersOnly/tutorSlots.html", {
        "slots": TutorSlot.objects.all().order_by("time"),
        "days": DAY_CHOICES,
        "times": TIME_CHOICES,
        "today": datetime.date.today().strftime('%A'),
    })