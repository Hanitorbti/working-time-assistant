from math import floor
from FileHandler import file_handler as file
from TTS import say
from tkinter import messagebox
from os import getcwd
from time import  localtime, strftime

the_time = localtime()
now_day = strftime("%d",the_time)
now_month = strftime("%m",the_time)
now_year = strftime("%y",the_time)

data = f"{getcwd()}//data"

timer = file(f"{data}//{now_year},{now_month},{now_day}.log")
timer = float(timer)

hour = int(floor(timer/60))
minute = int(timer % 60)

if hour == 0:
    messagebox.showinfo("Time Assistant",f"Time: {minute} Min")
    say(f"you are working for {minute} minute.")
else:
    messagebox.showinfo("Time Assistant",f"Time: {hour}:{minute}")
    say(f"you are working for {hour} hour and {minute} minute.")