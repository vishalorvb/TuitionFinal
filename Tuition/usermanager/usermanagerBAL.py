
from .usermanagerDAL import *
from .service import *
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
            AddUser(name=name, phone=phone, email=email, password=otp, points=2)
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

           