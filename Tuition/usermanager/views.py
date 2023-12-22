
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
import logging
from .usermanagerBAL import *
import urllib.parse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(process)d-%(levelname)s-%(message)s',
                    filename='../info.log', filemode='a', datefmt='%d-%b-%y %H:%M:%S')


def registration(request):
    if request.method == 'POST':
        try:
            full_name = request.POST['full_name']
            email = request.POST['email']
            phone_number = request.POST['phone_number']
            if saveUser(full_name, email, phone_number):
                request.session['phone_number'] = phone_number
                return HttpResponseRedirect(reverse('usermanager:verify_otp'))
            else:
                context = {"error": "Invalid phone Number or Email "}
                return render(request, 'usermanager/Registration.html', {"error": "Invalid phone Number or Email "})
        except Exception:
            logging.exception("Registration post request")
    return render(request, 'usermanager/Registration.html')


def login_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('Home:Home'))
    if request.method == 'POST':
        try:
            phone_number = request.POST['phone_number']
            if updatePassword(phone_number):
                request.session['phone_number'] = phone_number
                return HttpResponseRedirect(reverse('usermanager:verify_otp'))
            else:
                return render(request, 'usermanager/login.html', {'error': "Enter Valid Phone Number"})
        except Exception:
            logging.exception("Login page in view")
            return render(request, 'usermanager/login.html')
    return render(request, 'usermanager/login.html')


def verify_otp(request):
    if request.method == 'POST':
        password = str(request.POST['otp'])
        username = str(request.session['phone_number'])
        user = authenticate(request, phone_number=username, password=password)
        if user:
            del request.session['phone_number']
            login(request, user)
        else:
            return render(request, 'usermanager/Verify.html', {'error': 'Invalid OTP'})
        try:
            r = request.session['redirect_url_name']
            del request.session['redirect_url_name']
            return HttpResponseRedirect(reverse(r))
        except Exception:
            logging.exception("Not able to acces redirect url name")
            return HttpResponseRedirect(reverse('Home:Home'))
    try:
        check_session = request.session['phone_number']
        return render(request, 'usermanager/Verify.html')
    except Exception:
        logging.exception("Phone number not Exits in session")
        return HttpResponseRedirect(reverse('usermanager:login_page'))

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Home:Home'))


def verify_email(request,link):
    val = verifyEmail(urllib.parse.unquote(link))
    if val:
        return HttpResponse("Verified")
    else:
        return HttpResponse("Fail") 


#############################################################
######################## API ################################
#############################################################





@api_view(['POST'])
def createUser(request):
    try:
        full_name = request.data['full_name']
        email = request.data['email']
        phone_number = request.data['phone_number']
        if saveUser(full_name, email, phone_number):
            message = "User created successfully."
            return Response({"message": message}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Failed to create user."}, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
            logging.exception("Registration post request")
            return Response({"message": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
    


def updateProfile(request):
    pass


@api_view(['POST'])
def sendOtp(request):
    try:
        phone_number = request.data['phone_number']
        if updatePassword(phone_number):
            message = "OTP sent successfully."
            return Response({"message": message}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Failed to send OTP."}, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
            logging.exception("Registration post request")
            return Response({"message": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    user =  authenticate( phone_number=username, password=password)

    if user:
        refresh = RefreshToken.for_user(user)
        response_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user.id,
            'Full_name': user.Full_name,
        }
        return Response(response_data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)