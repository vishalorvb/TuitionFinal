from django.shortcuts import render
from .HomeBAL import *
from django.contrib.auth.decorators import login_required

def Home(request):
    tuitions = getTuition()
    return render(request,'Home/home.html',{'tuitions':tuitions})



@login_required(login_url="/usermanager/login")
def profile(request):
    mytution = getMytuition(request.user.id)
    mytuitionunlock = getMyUnlockTuition(request.user.id)
    myteacher = getmyteacher(request.user.id)
    print("my_teacher==============")
    print(myteacher)
    context = {"T":mytution,"UT":mytuitionunlock,"Teacher":myteacher}
    return render(request,'Home/profile.html',context)

def error(request):
    return render(request,'Home/Errorpage.html')


