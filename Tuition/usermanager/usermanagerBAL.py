
from .usermanagerDAL import *
from .service import *
from utility.useful import encryption
from django.conf import settings
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(process)d-%(levelname)s-%(message)s',filename='../info.log', filemode='a',datefmt='%d-%b-%y %H:%M:%S')


def sendVerificationLink(name,email,link):
    message = f'''
    Dear {name},

    Thank you for registering. Please click the link below to verify your account:
    http://127.0.0.1:8000/{link}

    Best regards,
    Home Tution
    '''
    send_Email('Account Verification',message,email)


def saveUser(name,email,phone):
    if IsPhoneNumberExist(phone) :
        logging.error("Phone number Already exist")
        return False
    if IsEmailExist(email):
        logging.error("Email Already exist")
        return False
    else:
        otp = send_otp(phone)
        if otp:
            id = AddUser(name=name, phone=phone, email=email, password=otp, points=2)
            link = encryption(settings.SECRET_KEY).encrypt_string(str(id))
            sendVerificationLink(name,[email],link)
            return True
        else:
            return False


def updatePassword(phone):    
    if IsPhoneNumberExist(phone) :
        otp = send_otp(phone)
        if otp:
            return update_password(phone,otp)     
        else:
            return False
    else:
        return False     

def is_tuitionid_exist(id):
    return IsTuitionIdExist(id)       

