from django.shortcuts import render
from .TeacherBAL import *
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseNotAllowed
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse


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


@login_required(login_url="/usermanager/login_page")
def unlock_teacher(request):
    if request.method == "GET":
        try:
            teacher_id = int(request.GET['teacher_id'])
            teacher = is_teacher_exist(teacher_id)
            if teacher == False:
                return HttpResponseRedirect(reverse('Home:error'))
        except:
            return HttpResponseRedirect(reverse('Home:error'))
        if request.user.credit_points > 0:
            unlock_teacherBAL(request.user, teacher)
            return HttpResponseRedirect(reverse('Home:profile'))
        else:
            # redirect to payment page
            return HttpResponseRedirect(reverse('payment:payment'))

    try:
        teacher_id = int(request.GET['teacher_id'])
        teacher = Teacher.objects.get(id=teacher_id)
        points = request.user.credit_points
        if points > 0:
            request.user.credit_points = points - 1
            request.user.save()
            Tu = Teacher_unlock.objects.create(
                Teacher_id=teacher, User_id=request.user)
            Tu.save()
            return HttpResponse(teacher.Phone_number)
        else:
            return HttpResponseRedirect(reverse('payment:create_order'))

    except:
        return HttpResponseRedirect(reverse('teacher:view_teacher'))


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
