from tkinter import *
from datetime import date

window = Tk()
window.title("Date Display")
window.geometry("300x200")
lbl = Label(text="hey there!",fg="blue",bg="yellow",height=5,width=20)
name = Label(text="full name",bg="blue")
namey = Entry()
def display():
    namey = name.get()
    