from .models import *
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(process)d-%(levelname)s-%(message)s',
                    filename='../info.log', filemode='a', datefmt='%d-%b-%y %H:%M:%S')


def addTuition(posted_date, user, student_name, phone_number, course, subject, description, teaching_mode, fee, pincode, locality):
    try:
        new_tuition = Tuitions.objects.create(
            posted_date=posted_date, user_id=user, student_name=student_name, phone_number=phone_number,course=course,subject=subject,description=description,teaching_mode=teaching_mode,fee=fee,pincode=pincode,locality=locality)
        return True
    except Exception:
        logging.exception("add tuition in tuition DAL")
        return False

def getLatestTuition():
    try:
        t = tuitions = Tuitions.objects.filter(status = True).order_by('-posted_date')[:10]
        return t
    except Exception:
        logging.exception("getlatestTuition")
        return False
        
def getAllTuition():
    try:
        t = tuitions = Tuitions.objects.filter(status = True).order_by('-posted_date')[:100]
        return t
    except Exception:
        logging.exception("getlatestTuition")   
        return False
        
def IsTuitionIdExist(id):
    try:
        return Tuitions.objects.get(id = id)
    except :
        return False
            
def unlockTuition(user,tuition):
    try:
        return Tuition_unlock.objects.create(User_id =user,Tuition_id = tuition)
    except Exception:
        logging.exception("UnlockTuition DAL")
        return False
        
           

