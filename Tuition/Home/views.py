from django.shortcuts import render
from .HomeBAL import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from usermanager.service import send_Email


def Home(request):
    tuitions = getTuition()
    # return HttpResponse("hello")
    return render(request,'Home/home.html',{'tuitions':tuitions})
    # return render(request,'Home/home.html')



@login_required(login_url="/usermanager/login")
def profile(request):
    mytution = getMytuition(request.user.id)
    mytuitionunlock = getMyUnlockTuition(request.user.id)
    myteacher = getmyteacher(request.user.id)
    context = {"T":mytution,"UT":mytuitionunlock,"Teacher":myteacher}
    return render(request,'Home/profile.html',context)


def editProfile(request):
    if request.method == "POST":
        user = request.user
        name = request.POST['name']
        file  = request.FILES['pic']
        file.name = str(user.id)+"__"+str(user.phone_number)
        print("======================",file.size)
        print("File is",dir(file))
        user.Full_name = name
        user.profilepic = file
        user.save()
        return render(request,'Home/profile.html')
    return render(request,'Home/updateProfile.html')
    
    



def error(request):
    return render(request,'Home/Errorpage.html')


def test(request):
    return HttpResponse("Hello")