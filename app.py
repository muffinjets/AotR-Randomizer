import tkinter as tk
from tkinter import filedialog, Text
import os

root = tkinter.Tk

canvas = tkinter.Canvas(root, height=700, width=700, bg="#00CC00")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
