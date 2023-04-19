from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app1.forms import *

def Student(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        FD=StudentForm(request.POST)
        if FD.is_valid():
            return HttpResponse(str(FD.cleaned_data))
    return render(request,'Student.html',d)