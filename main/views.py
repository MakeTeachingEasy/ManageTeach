from django.http.response import Http404, HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib.auth.models import User
from .models import AbsenceType, Student, Grade, Log
import datetime

MONTHS= ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# global variables -> non-constant
grade_values_raw = Grade.objects.order_by().values('grade').distinct()
grade_values = [ele['grade'] for ele in grade_values_raw]

# Create your views here.
def index(response):
    students_class_wise= {}
    for grade_value in grade_values:
        students_class_wise[grade_value]=(Student.objects.filter(grade=Grade.objects.get(grade=grade_value)).order_by("f_name"))
    return render(response, "main/home.html", {
        "classes": grade_values,
        "students": students_class_wise,
        "user": response.user,
    })

def studentDetails(response, id, month=datetime.date.today().month):
    if response.GET !={}:
        if response.GET.get("monthQ") in MONTHS:
            month= MONTHS.index(response.GET.get("monthQ"))+1
        
    student= Student.objects.get(id=id)
    presences= student.personal_logs.filter(is_present=True)
    informed= student.personal_logs.filter(is_present=False, AbsenceType=AbsenceType.objects.get(type="Informed"))
    uninformed= student.personal_logs.filter(is_present=False, AbsenceType=AbsenceType.objects.get(type="Uninformed"))
    return render(response, "main/studentDetails.html", {
        "student":student,
        "presences": presences.order_by("date").filter(date__month=month).reverse(),
        "informed":informed.order_by("date").filter(date__month=month).reverse(),
        "uninformed":uninformed.order_by("date").filter(date__month=month).reverse(),
        "user": response.user,
        "months": MONTHS,
        "this_month": MONTHS[month-1],
    })

def getRecords(response, year= datetime.date.today().year, month=datetime.date.today().month, day=datetime.date.today().day):
    if response.GET!={}:
        the_date= response.GET.get("dateQuery")
        if the_date !="":
            the_date=[int(ele) for ele in the_date.split("-")]
            year, month, day= the_date

    past_week_logs={}
    for i in range(0,7):
        date= datetime.date(year,month, day) + datetime.timedelta(days=-1*i)
        past_week_logs[date]= Log.objects.filter(date=date)

    return render(response, "main/records.html", {
        "start_date": datetime.date(year, month, day),
        "start_date_str": str(datetime.date(year,month,day)),
        "records": past_week_logs,
        "this_month": MONTHS[datetime.date(year,month,day).month-1],
        "uninformed": AbsenceType.objects.get(type="Uninformed"),
        "informed": AbsenceType.objects.get(type="Informed"),
    })

def error_404_view(response, exception):
    return render(response, "main/404.html",{} )