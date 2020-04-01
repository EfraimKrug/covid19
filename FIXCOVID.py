from datetime import *
from tkinter import *
from tkinter import filedialog
import tkMessageBox
import subprocess
import os

import time
from os import walk
import sys
import csv
import openpyxl
from openpyxl import Workbook
from functools import partial
import lookup
#########################################################
# get parent directory...
#########################################################

sys.path.append(os.getcwd())
sys.path.append(os.getcwd()[0:os.getcwd().rfind('\\')])


root = Tk()
# bgImage = PhotoImage(file=".\\MainBox\\KTMGate.PNG")
root.geometry('1600x800')
root.title('Looking up carona COVID-19')

def checkInput():
    subprocess.call([batdir + '\\checkInput.bat', 'Partial'], shell=False)


def getFilenames():
    f = []
    mypath = basedir

    for (dirpath, dirnames, filenames) in walk(mypath):
        f.extend(filenames)
    for x in f:
        if (x == 'yahrzeits.xlsx'):
            fname = mypath + r'\\shulCloud\\yahrzeits.xlsx'
            checkOldFile(fname)

def getFileAge(fileName):
    try:
        fileDate = time.ctime(os.path.getmtime(fileName))
        currDateDt = datetime.now()
        fileDateDt = datetime.strptime(fileDate, '%a %b %d %H:%M:%S %Y')
        return (currDateDt - fileDateDt).days
    except:
        return 365

def screen_list(return_list):
    color_flip = 0
    y_value = 111
    row_count = 0

    for e in return_list:
        sql = "SELECT * FROM Document WHERE ID = " + str(e[0])
        lookup.cur.execute(sql)
        rs = lookup.cur.fetchall()
        for rec in rs:
            if(rec[3] and row_count < 10):
                print(str(row_count) + "]]" + rec[3])
                row_count = row_count + 1
                if(color_flip):
                    labelEB1 = Label(frame, text=str(rec[3]), bg="black", fg="yellow", font='Helvetica 12')
                    labelEB1.pack(side=LEFT)
                    labelEB1.place(x=29, y=y_value, bordermode=OUTSIDE, height=25, width=1570)
                    color_flip = 0
                else:
                    labelEB1 = Label(frame, text=str(rec[3]), bg="black", fg="blue", font='Helvetica 12')
                    labelEB1.pack(side=LEFT)
                    labelEB1.place(x=29, y=y_value, bordermode=OUTSIDE, height=25, width=1570)
                    color_flip = 1
                y_value = y_value + 25


entryBox1 = ""
def look_up(arg):
    global entryBox1
    input_word = entryBox1.get()
    return_list = lookup.word_lookup(input_word.lower())
    screen_list(return_list)

def buildScreen():
    global labelMessage
    global entryBox1
    labelEB1 = Label(frame, text="Search: ", bg="black", fg="yellow", font='Helvetica 16')
    labelEB1.pack(side=RIGHT)
    labelEB1.place(x=9, y=50, bordermode=OUTSIDE, height=50, width=270)
    entryBox1 = Entry(frame, bg="black", fg="yellow", font='Helvetica 16')
    entryBox1.pack(side=RIGHT)
    entryBox1.place(x=229, y=50, bordermode=OUTSIDE, height=50, width=270)

    buttonGO = Button(frame, text='GO', bg='yellow', fg='red')
    buttonGO.pack(side=RIGHT)
    buttonGO.place(x=529, y=50, bordermode=OUTSIDE, height=50, width=50)

    # buttonD2 = Button(frame, text='Yahrzeit Names for Bulletin', bg='tan', fg='red')

    buttonGO.bind("<Leave>", look_up)
    # buttonD1.bind("<Leave>", eraseMessage)
    # buttonD2.bind("<Enter>", writeMessage02)
    # buttonD2.bind("<Leave>", eraseMessage)
    #
    # buttonD2.pack(side=RIGHT)
    #
    # buttonD1.place(x=75, y=50, bordermode=OUTSIDE, height=30, width=200)
    # buttonD2.place(x=75, y=90, bordermode=OUTSIDE, height=30, width=200)
    #
    # labelMessage = Label(frame, text="...message...", bg="black", fg="yellow", font='Helvetica 8')
    # labelMessage.pack(side=RIGHT)
    # labelMessage.place(x=1, y=350, bordermode=OUTSIDE, height=30, width=270)
    # # labelMessage.bind("<Enter>", writeMessage)
    # labelMessage.bind("<Leave>", eraseMessage)

frame = Frame(root, width=1580, height=790)
buildScreen()
frame.configure(background='black')
frame.pack()
root.mainloop()
