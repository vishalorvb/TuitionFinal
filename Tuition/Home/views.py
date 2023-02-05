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
    print(mytution)
    print("my unlocks")
    print(mytuitionunlock)
    for t in mytuitionunlock:
        print(t.Tuition_id.fee)
    context = {"T":mytution,"UT":mytuitionunlock}
    return render(request,'Home/profile.html',context)

def error(request):
    return render(request,'Home/Errorpage.html')


