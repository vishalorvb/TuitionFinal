
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
import logging
from .usermanagerBAL import *
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
            # This try block is to check if someone modify name's in form
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
        except:
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