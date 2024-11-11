from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

window=Tk()
window.title("Напоминание со звуком")

label=Label(text="Установите напоминание", font=("Courier", 20))
label.pack(pady=20)

button=Button(text="Установить", command=sett)
button.pack(pady=20)

window.mainloop()
