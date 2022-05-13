import tkinter as tk
from tkinter import filedialog
import randomizer

# Create a class named root that calls all of the tk functions
root = tk.Tk()
root.title('Attack of the Rhynocs Randomizer')
root.geometry('500x500')
root.iconbitmap("icon.ico")

frame = tk.Frame(root)
frame.pack(pady=10, padx=10)

# create a table that holds the rom loaded from the user
ROMs = []


# Prompts the user to load a .gba file
def loadROM():
    filename= filedialog.askopenfilename(initialdir="/", title="Select Attack of the Rhynocs (U) ROM",
                                        filetypes= (("GBA ROMs", "*.gba"), ("All files", "*.*")))
    ROMs.append(filename)
    print(filename)

def generateSeed():
        print("Generating Seed... (Currently no randomization functions written.)")



openROMButton = tk.Button(frame, text = "Open ROM")
openROMButton.grid(row = 0, column = 0, padx = 5, pady = 5, command=loadROM)
 
beginRandoButtton = tk.Button(frame, text = "Generate Game")
beginRandoButtton.grid(row = 0, column = 1, padx = 5, pady = 5, command=generateSeed)

root.mainloop()