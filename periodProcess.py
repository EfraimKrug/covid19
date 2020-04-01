FILE_NAME = '.runTrack'
from datetime import *

def getLastRun():
    try:
        fd = open(FILE_NAME, 'r')
    except Exception:
        longAgo = datetime.today() - timedelta(days = 28)
        storeThisRun(str(longAgo))
        fd = open(FILE_NAME, 'r')

    line = fd.readlines()[-1]
    print(line)
    lastRun = datetime.strptime(line[0:10], "%Y-%m-%d")
    fd.close()
    return lastRun

def getThisRun():
    thisRun = datetime.now()
    return thisRun

def storeThisRun(thisRun):
    fd = open(FILE_NAME, 'a')
    fd.write(thisRun + '\n')
    fd.close()

def checkDays(thisRun, lastRun, delay):
    dayCount = (thisRun - lastRun).days
    if dayCount < delay:
        return False
    return True

def runMonthly(runProcess):
    if checkDays(getThisRun(), getLastRun(), 27):
        storeThisRun(str(getThisRun()))
        runProcess()
    else:
        storeThisRun(str(getThisRun()) + " WAIT... Deal with yourself...")
        print ("This program has been run within the last month")

def runWeekly(runProcess):
    if checkDays(getThisRun(), getLastRun(), 5):
        storeThisRun(str(getThisRun()))
        runProcess()
    else:
        storeThisRun(str(getThisRun()) + " WAIT... Deal with yourself...")
        print ("This program has been run within the last week")

def runWhatever(runProcess, delay=15):
    if checkDays(getThisRun(), getLastRun(), delay):
        storeThisRun(str(getThisRun()))
        runProcess()
    else:
        storeThisRun(str(getThisRun()) + " WAIT... Deal with yourself...")
        print ("This program has been run within the last " + str(delay) + " days")


# usage:
# from periodProcess import *
#
# def runProcess():
#     print("Running... hah!")
#
# runMonthly(runProcess)
