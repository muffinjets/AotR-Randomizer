import tkinter as tk
from tkinter import PhotoImage, filedialog, Text
import randomizer

# Create a class named root that calls all of the tk functions
root = tk.Tk()
root.title('Attack of the Rhynocs Randomizer')
root.geometry('500x500')
root.iconbitmap("icon.ico")

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


# canvas = tk.Canvas(root, height=700, width=700, bg="#60E0C0")
# canvas.pack()

openROMButton = tk.Button(root, text="Open ROM", padx=10,
                    pady=0, fg="white", bg="#263D42", command=loadROM)
openROMButton.pack()

beginRandoButton = tk.Button(root, text="Generate Game", padx=10,
                    pady=0, fg="white", bg="#263D42", command=generateSeed)
beginRandoButton.pack()

root.mainloop()