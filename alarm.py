import time
import threading
from tkinter import *
from tkinter import messagebox
import pyttsx3

# Initialize the text-to-speech engine globally to avoid reinitializing it every time
alarm_engine = pyttsx3.init()

def check_alarm(alarm_time):
    print("Alarm set for:", alarm_time)  # Debug statement
    
    while True:
        current_time = time.strftime("%H:%M")
        print("Current time:", current_time)  # Debug statement
        if current_time == alarm_time:
            print("Alarm time reached!")  # Debug statement
            # Trigger the alarm in the main thread
            root.after(0, trigger_alarm)
            break
        time.sleep(1)

def trigger_alarm():
    print("Triggering alarm...")  # Debug statement
    voice = 'Time to wake up'
    alarm_engine.say(voice)
    alarm_engine.runAndWait()
    messagebox.showinfo("Alarm", "Time to wake up!",parent = root)

def set_alarm():
    alarm_time = entry.get()
    print("Alarm time entered:", alarm_time)  # Debug statement
    if not validate_time(alarm_time):
        messagebox.showerror("Invalid time", "Please enter a valid time in HH:MM format.")
        return
    else:
        print("Starting alarm thread")  # Debug statement
        t = threading.Thread(target=check_alarm, args=(alarm_time,))
        t.daemon = True
        t.start()
        print("Alarm thread started")  # Debug statement

def validate_time(alarm_time):
    try:
        time.strptime(alarm_time, "%H:%M")
        return True
    except ValueError:
        return False

# GUI setup
root = Tk()
root.title("ALARM")
root.geometry("500x500+300+50")

Label(root, text="Enter Alarm Time (HH:MM)", font=("Montserrat", 14)).place(relx=.2, rely=0.2)
entry = Entry(root, width=30, font=("Montserrat", 14), bd=2)
entry.place(relx=.1, rely=.3)

btn = Button(root, text="Set Alarm", font=("Montserrat", 14), bg="red", fg="white", width=25, command=set_alarm)
btn.place(relx=.2, rely=.5)

root.mainloop()
