from tkinter import *
from tkinter import messagebox
import time
import threading

def check_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            messagebox.showinfo('alarm','Time to wake up')
            break
        time.sleep(1)

def set_alarm():
    alarm_time = entry.get()
            


root = Tk()
root.title("ALARM")
root.geometry("500x500+300+50")

Label(root,text = "Enter Alarm Time(HH:MM)",font=("Montserrat",14)).place(relx=.2,rely = 0.2)
entry = Entry(root, width = 30,font=("Montserrat",14),bd = 2)
entry.place(relx = .1,rely =.3)

Button(root, text = "Set Alarm",font=("Montserrat",14),bg = "red",fg = "white",width = 25).place(relx =.2,rely = .5)


root.mainloop()