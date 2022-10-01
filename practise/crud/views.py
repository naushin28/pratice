from unicodedata import name
from django.shortcuts import render
from django.http import JsonResponse
from crud.models import Student

# Create your views here.
def getallstudnets(request):
    allstudents = Student.objects.all()
    
    alldata = []
    for singlestudent in allstudents:
        data={
            'name':singlestudent.name,
            'age':singlestudent.age,
            'isActive':singlestudent.isActive
        }
        alldata.append(data)
    print(alldata)

    return JsonResponse({'students':alldata})

def getactivestudnets(request):
    allstudents = Student.objects.filter(isActive=False)
    
    alldata = []
    for singlestudent in allstudents:
        data={
            'name':singlestudent.name,
            'age':singlestudent.age,
            'isActive':singlestudent.isActive
        }
        alldata.append(data)
    print(alldata)

    return JsonResponse({'students':alldata})

