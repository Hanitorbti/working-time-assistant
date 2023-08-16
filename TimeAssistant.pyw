from time import sleep as slp, localtime, strftime
from tkinter import messagebox
from win32ui import MessageBox
from os import system
from FileHandler import file_handler as file
from TTS import say
from WinNotif import ntf
from math import floor

the_time = localtime()
now_date = strftime("%d",the_time)

def counter():
    cnt = file("time.log")
    cnt = float(cnt)
    return cnt

def sleep():
    result = messagebox.askyesno("Time assistant", "Do you want to turn on rest mode?")
    if result:
        MessageBox("rest mode will turn on soon.", "Time Assistant")
        slp(7)
        system("rundll32.exe powrprof.dll, SetSuspendState Sleep")

    else:
        pass

date = file("date.log")
if date == "":
    file("date.log","w",now_date)

date = file("date.log")
if date != now_date:
    file("time.log","w","0")
    file("date.log","w",now_date)
else:
    pass

while True:
    slp(60)
    cnt0 = counter()
    file("time.log","w",f"{cnt0+1}")
    cnt0 = counter()
    hour = int(floor(cnt0/60))
    minute = int(cnt0 % 60)

    if cnt0 % 60 == 0 and cnt0 != 0:
        if cnt0 % 180 == 0 and cnt0 != 0:
            ntf(f"{hour} hour reminder")
            say(f"""Hani, You are working for {hour} hour. I think a some rest will be good for you.
                do you want to turn on the rest mode? """)
            sleep()
            
        else:
            ntf(f"{cnt0/60} hour reminder")
            say(f"Hani, You are working for {hour} hour. I think a some rest will be good for you.")

    elif cnt0 % 30 == 0 and cnt0 != 0:
        ntf(f"30 minute reminder")
        if hour == 0:
            say(f"so you passed an another half! you are working for {minute} minute.")
        else:
            say(f"so you passed an another half! you are working for {hour} hour and {minute} minute.")
    