from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseBadRequest,HttpResponseNotAllowed
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .tuitionBAL import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

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
            request.session['pincode'] = None
            request.session['locality'] = " "


            if request.POST['mode'] != "online":
                return HttpResponseRedirect(reverse('tuition:post_tuition_page2'))

            if request.user.is_authenticated:
                return save_tuition(request)
            else:
                request.session['redirect_url_name'] = 'tuition:save_tuition'
                return HttpResponseRedirect(reverse('usermanager:login_page'))
        except Exception:
            logging.exception("Error in Post request of post tuition page1 view")
            return HttpResponseRedirect(reverse('Home:error'))

    return render(request, 'Tuition/page1.html')



def post_tuition_page2(request):
    if request.method =="POST":
        try:
            request.session['pincode'] = request.POST['pincode']
            request.session['locality'] = request.POST['locality']
        except Exception:
            logging.exception("Accessing session in post tuition page 2")  
            return HttpResponseRedirect(reverse('tuition:page1'))  
        
        
        if request.user.is_authenticated:
            return save_tuition(request)
           
        else:
            request.session['redirect_url_name'] = 'tuition:save_tuition'
            return HttpResponseRedirect(reverse('usermanager:login_page'))
    try:
        x = request.session['pincode']
        return render(request, 'tuition/page2.html')

    except:
        # return HttpResponseRedirect(reverse('tuition:post_tuition_page1'))
        return render(request, 'tuition/page2.html')
        
    
    


def view_tuitions(request):
    tuitions = get_all_tuition()
    return render(request,'Tuition/Tuitions.html',{'tuitions':tuitions})


@login_required(login_url="/usermanager/login")
def unlock_tuition(request):
    if request.method == "GET":  
        try:
            tuition_id = request.GET['tuition_id']
            tution = is_tutionid_exists(tuition_id)
            logging.info("Calling view of unlock tuition")
            if tution :
                if request.user.credit_points > 0:
                    unlock_tuitions(request.user,tution)
                    return HttpResponseRedirect(reverse('Home:profile'))
                else:
                    return HttpResponseRedirect(reverse('payment:payment'))           
            else:
                return HttpResponseRedirect(reverse('Home:error'))
        except Exception:
            logging.exception("Unlock tution view")  

    return HttpResponseRedirect(reverse('Home:error'))
    
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
            pin = isPincodeExists(pincode)
            if pincode != None and pin == False:
                return render(request, 'tuition/page2.html',{"error": "Invalid Pincode "})
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
            
            t = saveTuition(request.user, student_name=student_name, phone_number=phone_number, course=course, subject=subject, description=description, teaching_mode=mode, fee=fee,pincode=pin,locality=locality)
            if t:
                return HttpResponseRedirect(reverse('Home:profile'))
            else:
                return HttpResponseRedirect(reverse('Home:error'))
        return HttpResponseRedirect(reverse('usermanager:login_page'))
    except Exception:
        logging.exception("save tuition")  
        return HttpResponseRedirect(reverse('Home:error'))
    
    
@login_required(login_url="usermanager/login_page")   
def change_status(request):
    if request.method == "GET": 
        try:
            tid = request.GET['tuition_id']
            t  = change_status_of_tuition(request.user.id,tid)
            if t:
                return HttpResponseRedirect(reverse('Home:profile'))
            else:
                return HttpResponseBadRequest("Not belongs to you")
        except Exception:
            logging.exception("change status of tuition")
            return HttpResponseRedirect(reverse('Home:error'))
    else:
        return HttpResponseNotAllowed("Method not allowed")
        


##################################################################################
################################## API ###########################################
##################################################################################
    
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def createTuition(request):
    try:
        student_name = request.data['student_name']
        phone_number = request.data['student_phone_number']
        course = request.data['course']
        subject = request.data['subject']
        description = request.data['description']
        fee = request.data['fee']
        mode = request.data['mode']
        pincode = request.data['pincode']
        locality = request.data['locality']
        pin = isPincodeExists(pincode)
    except:
        return Response({"message": "Invalid Data format."}, status=status.HTTP_400_BAD_REQUEST)
    if pin == False:
        return Response({"message": "Invalid pincode."}, status=status.HTTP_400_BAD_REQUEST)
    
    t = saveTuition(request.user, student_name=student_name, phone_number=phone_number, course=course, subject=subject, description=description, teaching_mode=mode, fee=fee,pincode=pin,locality=locality)

    if t:
        return Response({"message": "Your Tuition Posted Successfully."}, status=status.HTTP_201_CREATED)
    return Response({"message": "Failed to create."}, status=status.HTTP_400_BAD_REQUEST)






@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def unlockTuition(request):
    try:
        tuition_id = request.data['tuition_id']
        contact = unlock_tuitions(request.user,tuition_id)
        if contact:
            return Response({"message": contact}, status=status.HTTP_200_OK)
        Response({"message": "Failed to get contact."}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({"message": "Invalid Data."}, status=status.HTTP_400_BAD_REQUEST)





@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def changeStatus(request):
    try:
        tid = request.GET['tuition_id']
        t  = change_status_of_tuition(request.user.id,tid)
        if t:
            return Response({"message": "Opration Successfull."}, status=status.HTTP_200_OK)
        Response({"message": "Failed."}, status=status.HTTP_400_BAD_REQUEST)

    except:
        Response({"message": "Invalid Data."}, status=status.HTTP_400_BAD_REQUEST)

