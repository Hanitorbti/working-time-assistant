from math import floor
from FileHandler import file_handler as file
from TTS import say
from tkinter import messagebox

timer = file("time.log")
timer = float(timer)

hour = int(floor(timer/60))
minute = int(timer % 60)

if hour == 0:
    messagebox.showinfo("Time Assistant",f"Time: {minute} Min")
    say(f"you are working for {minute} minute.")
else:
    messagebox.showinfo("Time Assistant",f"Time: {hour}:{minute}")
    say(f"you are working for {hour} hour and {minute} minute.")