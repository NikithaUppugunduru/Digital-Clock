from tkinter import Tk
from tkinter import Label
import time
import sys

main=Tk()
main.title("Digital Clock")
def get_time():
    timeVar=time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200,get_time)


clock=Label(main,font=("Times New Roman",50),bg="grey",fg="white")
clock.pack()
get_time()
main.mainloop()