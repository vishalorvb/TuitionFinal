from django.shortcuts import render
from .HomeBAL import *

def Home(request):
    tuitions = getTuition()
    return render(request,'Home/home.html',{'tuitions':tuitions})



def error(request):
    return render(request,'Home/Errorpage.html')


def profile(request):
    return render(request,'Home/profile.html')