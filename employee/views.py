from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee
# Create your views here.


def home(request):
      return render(request, "employee/home.html")




def allemployees(request):
    e = Employee.objects.all()
    return render(request, "employee/allemployees.html", {"employees":e})




def singleemployee(request, empid):
    e = Employee.objects.get(pk = empid)
    return render(request, "employee/singleemployee.html", {"emp" : e})



def addemployee(request):
    if request.method == "POST":
        #take all the parameters value from request through form.
             
            empID = request.POST.get('empID')
            empName = request.POST.get('empName')
            empEmail = request.POST.get('empEmail')
            empAddress = request.POST.get('empAddress')
            empPhone = request.POST.get('empPhone')

            # save these values to employee model means database

            e = Employee()
            e.empID = empID
            e.empName = empName
            e.empEmail = empEmail
            e.empAddress = empAddress
            e.empPhone = empPhone
            e.save()
            return redirect("addemployee")
    
    return render(request, "employee/addemployee.html")



def deleteemployee(request, empid):
     e = Employee.objects.get(pk  = empid)
     e.delete()
     return redirect("allemployees")




def updateemployee(request, empid):
     if request.method == "POST":
        #take all the parameters value from request through form.
             
            empID = request.POST.get('empID')
            empName = request.POST.get('empName')
            empEmail = request.POST.get('empEmail')
            empAddress = request.POST.get('empAddress')
            empPhone = request.POST.get('empPhone')

            emp  = Employee.objects.get(pk = empid)
            emp.empID = empID
            emp.empName = empName
            emp.empEmail = empEmail
            emp.empAddress = empAddress
            emp.empPhone = empPhone
            emp.save()
            return redirect("allemployees")

     e  = Employee.objects.get(pk = empid)

     return render(request, "employee/updateemployee.html", {"emp":e})
