from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .tuitionBAL import *

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(process)d-%(levelname)s-%(message)s',
                    filename='../info.log', filemode='a', datefmt='%d-%b-%y %H:%M:%S')

def post_tuition_page1(request):
    if request.method == "POST":
        try:
            request.session['student_name'] = request.POST['student_name']
            request.session['student_phone_number'] = request.POST['student_phone_number']
            request.session['course'] = request.POST['course']
            request.session['subject'] = request.POST['subject']
            request.session['description'] = request.POST['description']
            request.session['fee'] = request.POST['fee']
            request.session['mode'] = request.POST['mode']
            request.session['pincode'] = 0000
            request.session['locality'] = " "


            if request.POST['mode'] == "offline":
                return HttpResponseRedirect(reverse('tuition:post_tuition_page2'))

            if request.user.is_authenticated:
                save_tuition(request)
            else:
                request.session['redirect_url_name'] = 'tuition:save_tuition'
                return HttpResponseRedirect(reverse('usermanager:login_page'))
        except Exception:
            logging.exception("Error in Post request of post tuition page1 view")
            return HttpResponseRedirect(reverse('Home:error'))

    return render(request, 'Tuition/post_tuition_page1.html')



def post_tuition_page2(request):
    if request.method =="POST":
        try:
            request.session['pincode'] = request.POST['pincode']
            request.session['locality'] = request.POST['locality']
        except Exception:
            logging.exception("Accessing session in post tuition page 2")  
            return HttpResponseRedirect(reverse('tuition:post_tuition_page1'))  
        
        
        if request.user.is_authenticated:
            return save_tuition(request)
           
        else:
            request.session['redirect_url_name'] = 'tuition/save_tuition'
            return HttpResponseRedirect(reverse('usermanager:login_page'))
    try:
        x = request.session['student_name']
        return render(request, 'tuition/post_tuition_page2.html')

    except:
        return HttpResponseRedirect(reverse('tuition:post_tuition_page1'))
    
    


def view_tuitions(request):
    tuitions = get_all_tuition()
    return render(request,'Tuition/Tuitions.html',{'tuitions':tuitions})


@login_required(login_url="/usermanager/login")
def unlock_tuition(request):
    if request.method == "GET":  
        try:
            tuition_id = request.GET['tuition_id']
            tution = is_tutionid_exists(tuition_id)
            if tution :
                if request.user.credit_points > 0:
                    unlock_tuition(request.user,tution)
                    return HttpResponse("Unlock tut")
            else:
                pass
        except:
            pass
        
    # tuition_id = request.GET['tuition_id']
    # tuition = Tuitions.objects.get(id = tuition_id)
    
    # points = request.user.credit_points
    # print("credit point is",points)
    # if  points > 0:
    #     request.user.credit_points = points - 1
    #     request.user.save()
    #     print(request.user.credit_points)
    #     tu = Tuition_unlock.objects.create(User_id = request.user , Tuition_id = tuition)
    #     contact = tuition.phone_number
    #     return HttpResponse(contact)
    # return HttpResponseRedirect(reverse('payment:create_order'))
    return HttpResponse("Unlock tut")
    
def save_tuition(request):
    try:
        if request.user.is_authenticated:
        
            student_name = request.session['student_name']
            phone_number = request.session['student_phone_number']
            course = request.session['course']
            subject = request.session['subject']
            description = request.session['description']
            fee = request.session['fee']
            mode = request.session['mode']
            pincode = request.session['pincode']
            locality = request.session['locality']
            
            # Deleting session
            del(request.session['student_name'] )
            del(request.session['student_phone_number'] )
            del(request.session['course'] )
            del(request.session['subject'])
            del(request.session['description'])
            del(request.session['fee'] )
            del(request.session['mode'])
            del(request.session['pincode']) 
            del(request.session['locality']) 
            
            saveTuition(request.user, student_name=student_name, phone_number=phone_number, course=course, subject=subject, description=subject, teaching_mode=mode, fee=fee,pincode=pincode,locality=locality)
            #write here where to redirect after login
            return HttpResponse("tuition saved")
        return HttpResponse("not saved login first")
    except Exception:
        logging.exception("save tuition")  
        return HttpResponseRedirect(reverse('tuition:post_tuition_page1'))
    