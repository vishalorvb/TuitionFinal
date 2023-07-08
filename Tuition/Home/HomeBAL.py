from Tuitionmanager.tuitionDAL import *
from Teacher.TeacherDAL import getMyTeacher

def getTuition():
    t = getLatestTuition()
    return t


def getMytuition(userid):
    return MyTuition(userid)


def getMyUnlockTuition(userid):
    return Myunlocks(userid)

def getmyteacher(userid):
    return getMyTeacher(userid)

