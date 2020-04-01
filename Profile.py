import os

cwd = os.getcwd()
########################################################
batdir = r'./bat'
basedir = r'.'
yahrdir = r'./yahr'
downloadPath = r'C:\\Users\\KTM\\Downloads\\'

dailyLogDir = r'C:\\Users\\KTM\\BOOKS'
depositDir = r'C:\\Users\\KTM\\BOOKS\\Checks\\Deposits\\'
checkDir = "C:\\Users\\KTM\\BOOKS\\Checks\\"
scanDir = "C:\\Users\\KTM\\Documents\\Scan\\"

# Find Downloads folder
def hasDownloads():
    try:
        os.chdir('Downloads')
        return True
    except:
        os.chdir('..')
        return False

def getRootDirectory():
    global basedir, downloadPath, checkDir, depositDir, dailyLogDir, batdir
    global cwd

    while len(os.getcwd().split('\\')) > 1:
        if hasDownloads():
            downloadPath = os.getcwd()
            os.chdir('..')
            basedir = os.getcwd() + r'\\KTMUtils\\msutils'
            batdir = basedir + r'\\bat'
            dailyLogDir = basedir + r'\\BOOKS\\DATA'
            checkDir = dailyLogDir + r'\\Checks'
            depositDir = checkDir + r'\\Deposits'
            os.chdir(basedir)
            return
    os.chdir(cwd)


# AcrobatPath = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
AcrobatPath = ""
server = ''

fromaddr = 'KadimahTorasMoshe@gmail.com'
username = 'KadimahTorasMoshe@gmail.com'
password = 'KTMS4@r0n'
smtpvar = 'smtp.gmail.com:587'

getRootDirectory()
# print('basedir: ' + basedir)
# print('batdir: ' + batdir)
#
# print('downloadPath: ' + downloadPath)
# print('dailyLogDir: ' + dailyLogDir)
# print('checkDir: ' + checkDir)
# print('depositDir: ' + depositDir)
# print('current working: ' + os.getcwd())
