from .models import *
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(process)d-%(levelname)s-%(message)s',filename='../info.log', filemode='a',datefmt='%d-%b-%y %H:%M:%S')


def IsPhoneNumberExist(phoneNumber):
    try:
        CustomUser.object.get(phone_number = phoneNumber)
        return True
    except Exception:
        logging.exception("DAL IsphonenumberExist")
        False


def IsEmailExist(email):
    try:
        CustomUser.object.get(email = email)
        return True
    except Exception :
        logging.exception("DAL IsEmailExist")
        False

def AddUser(name,email,password,phone,points):
    try:
        CustomUser.object.create_user(Full_name=name, phone_number=phone, email=email, password=password, credit_points=points)
    except Exception:
        logging.exception("password not update in DAL")
        
        
def update_password(phone,password):
    try:
        user =  CustomUser.object.get(phone_number = phone)
        user.set_password(password)
        user.save()
        
        logging.info("password updated")
        logging.info(user.phone_number)
        return True
    except Exception:
        logging.exception("password not update in DAL")
        return False
       
# def updateCredit(user):
#     try:
#         u = CustomUser.object.get(id = )       