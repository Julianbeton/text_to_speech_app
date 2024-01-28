import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("TEXT TO SPEECH")
root.geometry("900x450")
root.resizable(False,False)
root.configure(bg="#305065")

#icon
image_icon = PhotoImage(file="speak.png")
root.iconphoto(False, image_icon)

#Top Frame
Top_frame = Frame(root,bg = "white", width = 900, height = 100)
Top_frame.place(x = 0, y = 0)












root.mainloop()