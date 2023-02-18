from .tuitionDAL import *
from datetime import date
logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(process)d-%(levelname)s-%(message)s',
                    filename='../info.log', filemode='a', datefmt='%d-%b-%y %H:%M:%S')


def saveTuition(user, student_name, phone_number, course, subject, description, teaching_mode, fee, pincode=0000, locality= ''):
    try:
        posted_date = date.today()
        return addTuition(posted_date, user, student_name, phone_number, course, subject, description, teaching_mode, fee, pincode, locality)
    except Exception:
        logging.exception("saveTuition in tuitionBAL")
        return False



def get_latest_tuition():
    # return first 10 tuitions only
    return getLatestTuition()

def get_all_tuition():
    return getAllTuition()

def unlock_tuitions(user,tution):
    logging.info("Calling  BAL")
    if IstuitionUserExist(user.id,tution.id) == False and user.id != tution.user_id.id and user.credit_points > 0:
        if unlockTuition(user,tution):  
           cp = user.credit_points
           user.credit_points = cp -1
           user.save()
           return True
        else:
           return False  
    else:
        return True
    
        

def is_tutionid_exists(id):
    return IsTuitionIdExist(id)


def change_status_of_tuition(userid,tutionid):
    pair = IsTuitionBelongsToUser(userid,tutionid)
    if pair:
        changeStatus(tutionid)
        return True
    else:
        return False
    
        
        
