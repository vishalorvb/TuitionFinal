from django.shortcuts import render
from .HomeBAL import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from usermanager.service import send_Email
from PIL import Image,ImageOps
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


def Home(request):
    tuitions = getTuition()
    return render(request,'Home/home.html',{'tuitions':tuitions})



@login_required(login_url="/usermanager/login")
def profile(request):
    mytution = getMytuition(request.user.id)
    mytuitionunlock = getMyUnlockTuition(request.user.id)
    myteacher = getmyteacher(request.user.id)
    context = {"T":mytution,"UT":mytuitionunlock,"Teacher":myteacher}
    return render(request,'Home/profile.html',context)


@login_required(login_url="/usermanager/login")
def editProfile(request):
    if request.method == "POST":
        user = request.user
        name = request.POST['name']
        if len(request.FILES) > 0:   
            file  = request.FILES['pic']
            file =reSizeImage(file,(500, 500))
            file.name = str(user.id)+"__"+str(user.phone_number)
            user.profilepic = file
        user.Full_name = name
        user.save()
        return render(request,'Home/profile.html')
    return render(request,'Home/updateProfile.html')
    
    



def error(request):
    return render(request,'Home/Errorpage.html')


def test(request):
    return HttpResponse("Hello")




def reSizeImage(input_image, output_size):
        image = Image.open(input_image)
        image = ImageOps.exif_transpose(image)
        image.thumbnail(output_size)
        image_io = BytesIO()
        image.save(image_io, format='JPEG')
        resized_image = InMemoryUploadedFile(
            image_io,
            None,
            'resized_image.jpg',
            'image/jpeg',
            image_io.tell(),
            None
        )
        return resized_image

 