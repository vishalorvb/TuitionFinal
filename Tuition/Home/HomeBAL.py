from Tuitionmanager.tuitionDAL import *


def getTuition():
    t = getLatestTuition()
    return t


def getMytuition(userid):
    return MyTuition(userid)


def getMyUnlockTuition(userid):
    return Myunlocks(userid)
