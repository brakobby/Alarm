from tkinter import *
from tkinter import messagebox
import time
import threading

def check_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            messagebox.showinfo('alarm','Time to wake up')
            