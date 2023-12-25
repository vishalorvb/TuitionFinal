from django.shortcuts import render
from .TeacherBAL import *
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseNotAllowed
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import TeacherSerializer

def teacher_page1(request):
    if request.user.is_authenticated and is_user_teacher(request.user.id):
        return HttpResponseRedirect(reverse('teacher:teacher_profile'))
    if request.method == 'POST':
        try:
            request.session['name'] = request.POST['teacher_name']
            request.session['mode'] = request.POST['teacher_mode']
            request.session['subject'] = request.POST['teacher_subject']
            request.session['class'] = request.POST['teacher_class']
            return HttpResponseRedirect(reverse('teacher:teacher_page2'))
        except Exception:
            logging.exception("Name error in view")
            return HttpResponseRedirect(reverse('Home:error'))
    return render(request, 'Teacher/page1.html')


def teacher_page2(request):
    if request.method == 'POST':
        try:
            request.session['gender'] = request.POST['gender']
            request.session['experience'] = request.POST['experience']
            request.session['location'] = request.POST['location']
            request.session['qualification'] = request.POST['qualification']
            request.session['about'] = request.POST['about']
            request.session['age'] = request.POST['age']
            request.session['fee'] = request.POST['fee']
            request.session['pincode'] = request.POST['pincode']
            # request.session['teacher_phone_number']=request.POST['teacher_phone_number']
        except Exception:
            logging.exception("Name error in view")
            return HttpResponseRedirect(reverse('Home:error'))

        if request.user.is_authenticated:
            return Create_teacher(request)
        else:
            request.session['redirect_url_name'] = '/teacher/create_teacher'
            return HttpResponseRedirect(reverse('usermanager:login_page'))
    try:
        x = request.session['name']
        return render(request, 'Teacher/page2.html')
    except:
        return HttpResponseRedirect(reverse('teacher:teacher_page1'))


#@login_required(login_url="/usermanager/login_page")
#def unlock_teacher(request):
#    if request.method == "GET":
#        try:
#            teacher_id = int(request.GET['teacher_id'])
#            teacher = is_teacher_exist(teacher_id)
#            if teacher == False:
#                return HttpResponseRedirect(reverse('Home:error'))
#        except:
#            return HttpResponseRedirect(reverse('Home:error'))
#        if request.user.credit_points > 0:
#            unlock_teacherBAL(request.user, teacher)
#            return HttpResponseRedirect(reverse('Home:profile'))
#        else:
#            # redirect to payment page
#            return HttpResponseRedirect(reverse('payment:payment'))

#    try:
#        teacher_id = int(request.GET['teacher_id'])
#        teacher = Teacher.objects.get(id=teacher_id)
#        points = request.user.credit_points
#        if points > 0:
#            request.user.credit_points = points - 1
#            request.user.save()
#            Tu = Teacher_unlock.objects.create(
#                Teacher_id=teacher, User_id=request.user)
#            Tu.save()
#            return HttpResponse(teacher.Phone_number)
#        else:
#            return HttpResponseRedirect(reverse('payment:create_order'))

#    except:
#        return HttpResponseRedirect(reverse('teacher:view_teacher'))


def view_teacher(request):
    Teachers = get_latest_teacher()
    return render(request, 'Teacher/view_teacher.html', {'Teachers': Teachers})


def Create_teacher(request):
    try:
        if request.user.is_authenticated:
            if is_user_teacher(request.user.id):
                return HttpResponseRedirect(reverse('teacher:teacher_profile'))
            Name = request.session['name']
            Gender = request.session['gender']
            Experience = request.session['experience']
            location = request.session['location']
            Qualification = request.session['qualification']
            Subject = request.session['subject']
            classes = request.session['class']
            About = request.session['about']
            User_id = request.user
            Teaching_mode = request.session['mode']
            Age = request.session['age']
            Fee = request.session['fee']
            Pincode = request.session['pincode']
            pin = None if isPincode(Pincode)==False else isPincode(Pincode) 
            # request.session.clear()
            del request.session['gender']
            del request.session['experience']
            del request.session['location']
            del request.session['qualification']
            del request.session['about']
            del request.session['name']
            del request.session['mode']
            del request.session['subject']
            del request.session['class']
            del request.session['age']
            del request.session['fee']
            del request.session['pincode']
            teacher = save_teacher(Name=Name, Gender=Gender, Experience=Experience,
                                   Location=location, Qualification=Qualification, Subject=Subject, classes=classes,
                                   About=About, User_id=User_id, Teaching_mode=Teaching_mode,
                                   Phone_number=request.user.phone_number,
                                   Age=Age, Fee=Fee, Pincode=pin)
            if teacher:
                return HttpResponseRedirect(reverse('Home:profile'))
            else:
                logging.info("Wrong in create teacher in view")
                return HttpResponseRedirect(reverse('Home:error'))
        return HttpResponseRedirect(reverse('usermanager:login_page'))
    except Exception:
        logging.exception("create teacher in view")
        return HttpResponseRedirect(reverse('Home:error'))


@login_required(login_url="/usermanager/login_page")
def Teacher_Profile(request):
    Teacher = is_user_teacher(request.user.id)
    if Teacher == False:
        return HttpResponseRedirect(reverse('teacher:teacher_page1'))
    if request.method == 'POST':
        try:
            Teacher.Name = request.POST['name']
            Teacher.Experience = request.POST['experience']
            Teacher.Location = request.POST['locality']
            Teacher.Qualification = request.POST['qualification']
            Teacher.Subject = request.POST['subject']
            Teacher.classes = request.POST['classes']
            Teacher.Pincode =None if isPincode(request.POST['pincode'])==False else isPincode(request.POST['pincode'])
            Teacher.Teaching_mode = request.POST['mode']
            Teacher.Age = request.POST['age']
            Teacher.About = request.POST['about']
            Teacher.save()
            return HttpResponseRedirect(reverse('Home:profile'))
        except Exception:
            logging.exception("create teacher in view")
            return HttpResponseRedirect(reverse('Home:error'))
    print(Teacher.Name)
    return render(request, 'Teacher/TeacherProfile.html', {"Teacher": Teacher})


#############################################################
########################### API #############################
#############################################################



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_teacher(request):
    Teacher = is_user_teacher(request.user.id)
    if Teacher:
        return Response({"message": "Already Exists."}, status=status.HTTP_400_BAD_REQUEST)
    try:
        Name = request.data['teacher_name']
        Gender = request.data['gender']
        Experience = request.data['experience']
        Location = request.data['location']
        Qualification = request.data['qualification']
        Subject = request.data['subject']
        classes = request.data['classes']
        About = request.data['about']
        User_id = request.user
        Teaching_mode = request.data['mode']
        Age = request.data['age']
        Fee = request.data['fee']
        Pincode = request.data['pincode']
        pin = None if isPincode(Pincode)==False else isPincode(Pincode)
        
        teacher = save_teacher(Name=Name, Gender=Gender, Experience=Experience,
                                   Location=Location, Qualification=Qualification, Subject=Subject, classes=classes,
                                   About=About, User_id=User_id, Teaching_mode=Teaching_mode,
                                   Phone_number=request.user.phone_number,
                                   Age=Age, Fee=Fee, Pincode=pin)
        if teacher:
            message = "Created successfully."
            return Response({"message": message}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Failed to create."}, status=status.HTTP_400_BAD_REQUEST)

    except:
        logging.exception("Registration post request")
        return Response({"message": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_teacher_Profile(request):
    Teacher = is_user_teacher(request.user.id)
    if Teacher == False:
        return Response({"message": "User is not a teacher."}, status=status.HTTP_400_BAD_REQUEST)
    try:
        Teacher.Name = request.data['name']
        Teacher.Experience = request.data['experience']
        Teacher.Location = request.data['locality']
        Teacher.Qualification = request.data['qualification']
        Teacher.Subject = request.data['subject']
        Teacher.classes = request.data['classes']
        Teacher.Pincode =None if isPincode(request.data['pincode'])==False else isPincode(request.data['pincode'])
        Teacher.Teaching_mode = request.data['mode']
        Teacher.Age = request.data['age']
        Teacher.About = request.data['about']
        Teacher.save()
        return Response({"message": "Teacher Profile Updated."}, status=status.HTTP_202_ACCEPTED)
    except Exception:
        logging.exception("create teacher in view")
        return Response({"message": "Internal Server Error, Invalid Data."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getTecher_info(request):
    teacher = getTeacheInfo(request.user.id)
    if teacher == None:
        return Response({"message": "Teacher Not Exists."}, status=status.HTTP_400_BAD_REQUEST)
    serializer = TeacherSerializer(teacher)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def unlock_teacher(request):
    user = request.user
    teacherId = request.data["teacher_id"]
    unlock = unlock_teacherBAL(user,teacherId)
    if unlock:
        return Response({"message": "Techer Unlock Successfully."}, status=status.HTTP_200_OK)
    return Response({"message": "No Credit Left."}, status=status.HTTP_400_BAD_REQUEST)
