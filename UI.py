import tkinter as tk
from tkinter import *
from tkinter import filedialog
import hashlib
import random


# Create a variable named root that holds/controls all tkinter functions
root = tk.Tk()
root.title('Attack of the Rhynocs Randomizer')
root.grid()
root.geometry('450x70')
root.iconbitmap("icon.ico")

frame = tk.Frame(root)
frame.grid(columnspan=4, row=1)  # Don't touch this line of code ever :gun_emoji:

correctROMBool = 0
ROM = 0
seedEntryBox = tk.StringVar()
settingsFlags = 0
quickEscapeStart = tk.IntVar()
generateSpoilerLog = tk.IntVar()


# Prompts the user to load a .gba file and checks if the md5 checksum hash is correct
def loadROM():
    global ROM
    validmd5 = "4a15b07b4dc292e9003c377c55372287"
    ROM = filedialog.askopenfile(title="Select Attack of the Rhynocs (U) ROM",mode="rb",
                                filetypes= (("GBA ROMs", "*.gba"), ("All files", "*.*")))
    if ROM != None:
        print("Loaded ROM")
        # read contents of file
        data = ROM.read()
        #pipe contents of the file through
        md5Returned = hashlib.md5(data).hexdigest()
        print("Checking ROM...")
        global correctROMBool
        if validmd5 == md5Returned:
            print ("Valid ROM.")
            correctROMBool = 1
            print("correctROMBool = ", int(validmd5 == md5Returned))
        else:
            print ("Invalid ROM, please try again.")
            correctROMBool = 0
            print("correctROMBool = ", int(validmd5 == md5Returned))
    elif ROM == None:
        print("No ROM detected. Please try again.")
        correctROMBool == 0
        print("correctROMBool = ", correctROMBool)

        


def generateGame():
    # print filepath of rom
    print("ROM = ",ROM)
    # grab seed value inputted by user, turn spinbox value into an integer
    seed = int(seedEntryBox.get())
    # "Is this the correct ROM?"
    global correctROMBool
    if correctROMBool == 1:
        print("Generating Seed... (Currently no randomization functions written.)")
        print("Seed Inputted =",seed)
        if seed == 0:
            seed = random.randrange(0,100000,1)
            print("Random Seed = ", seed)







        elif seed != 0:
            print("Manual Seed = ", seed)
    else:
        print("Please open Spyro: Attack of the Rhynocs (U) ROM file.")
        


openROMButton = tk.Button(root, text="Open ROM", fg="white", bg="#263D42", command=loadROM)
seedEntryLabel = tk.Label(root, text="Seed(Leave 0 for random):")
seedEntryBox = Spinbox(root, from_= 0, to = 99999, wrap=True)
generateSeedButton = tk.Button(root, text="Generate Game", padx=10, fg="white", bg="#263D42", command=generateGame)

quickEscapeStartCheck = tk.Checkbutton(frame, text="Start with Quick Escape", variable=quickEscapeStart, onvalue=1, offvalue=0)
generateSpoilerLogCheck = tk.Checkbutton(frame, text="Generate Spoiler Log", variable=generateSpoilerLog, onvalue=1, offvalue=0)



openROMButton.grid(column=0, row=0)
seedEntryLabel.grid(column=1, row=0)
seedEntryBox.grid(column=2, row=0)
generateSeedButton.grid(column=3, row=0)

quickEscapeStartCheck.grid(column=0, row=1, padx=0)
generateSpoilerLogCheck.grid(column=2, row=1, padx=0)





root.mainloop()