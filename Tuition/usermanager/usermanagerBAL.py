
from .usermanagerDAL import *
from .service import *
from utility.useful import encryption
from django.conf import settings
from .emailService import sendVerificationLink
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(process)d-%(levelname)s-%(message)s',filename='../info.log', filemode='a',datefmt='%d-%b-%y %H:%M:%S')



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
            link = encryption(settings.SECRET_KEY).encrypt_string(str(phone))
            AddUser(name=name, phone=phone, email=email, password=otp, points=2,link=link)
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


def verifyEmail(link):
    if link != None:
       return verify_email(link)
    else:
        return False
    


