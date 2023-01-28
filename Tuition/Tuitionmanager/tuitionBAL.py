from .tuitionDAL import *
from datetime import date
logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(process)d-%(levelname)s-%(message)s',
                    filename='../info.log', filemode='a', datefmt='%d-%b-%y %H:%M:%S')


def saveTuition(user, student_name, phone_number, course, subject, description, teaching_mode, fee, pincode=0000, locality= ''):
    try:
        posted_date = date.today()
        addTuition(posted_date, user, student_name, phone_number, course, subject, description, teaching_mode, fee, pincode, locality)
    except Exception:
        logging.exception("saveTuition in tuitionBAL")


def get_latest_tuition():
    # return first 10 tuitions only
    return getLatestTuition()

def get_all_tuition():
    return getAllTuition()

def unlock_tuition(user,tutionid):
    
    return unlockTuition(user,tutionid)

def is_tutionid_exists(id):
    return IsTuitionIdExist(id)