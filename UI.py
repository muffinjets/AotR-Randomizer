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
settingsFlags = 1

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

def escapeField():
    global settingsFlags
    escape = int(quickEscapeStart.get())
    if escape == 1:
        settingsFlags *= 2
        print("Settings Flags =", int(settingsFlags))
    if escape == 0:
        settingsFlags /= 2
        print("Settings Flags =", int(settingsFlags))

def spoilerField():
    global settingsFlags
    spoiler = int(generateSpoilerLog.get())
    if spoiler == 1:
        settingsFlags *= 4
        print("Settings Flags =", int(settingsFlags))
    elif spoiler == 0:
        settingsFlags /= 4
        print("Settings Flags =", int(settingsFlags))
    
        
##################################################################
#      When you want to make new settings use this template      #
##################################################################

# longCamelCaseName = tk.IntVar()

# def setting3Field():
#     global settingsFlags
#     shortname = int(longCamelCaseName.get())
#     if shortname == 1:
#         settingsFlags *= 8
#         print("Settings Flags =", int(settingsFlags))
#     elif shortname == 0:
#         settingsFlags /= 8
#         print("Settings Flagss =", int(settingsFlags))

# setting3Check = tk.Checkbutton(frame, text="Setting 3", variable=longCamelCaseName, command=setting3Field)
# setting3Check.grid(column=3, row=1, padx=0)


def generateGame():
    # print filepath of rom
    print("ROM = ",ROM)
    # grab seed value inputted by user, turn spinbox value into an integer
    seed = int(seedEntryBox.get())
    # "Is this the correct ROM?"
    global correctROMBool
    if correctROMBool == 1:
        if seed == 0:
            seed = random.randrange(0,100000,1)
            print("Random Seed = ", seed)

        # HAND IT OFF TO ANOTHER SCRIPT/FILE, KEEP THIS ONE SIMPLE

        elif seed != 0:
            print("Manual Seed = ", seed)
    else:
        print("Please open Spyro: Attack of the Rhynocs (U) ROM file.")
    return seed
        


openROMButton = tk.Button(root, text="Open ROM", fg="black", bg="#71e9c8", command=loadROM)
seedEntryLabel = tk.Label(root, text="Seed(Leave 0 for random):")
seedEntryBox = Spinbox(root, from_= 0, to = 99999, wrap=True)
generateSeedButton = tk.Button(root, text="Generate Game", padx=10, fg="black", bg="#71e9c8", command=generateGame)

quickEscapeStartCheck = tk.Checkbutton(frame, text="Start with Quick Escape", variable=quickEscapeStart, command=escapeField)
generateSpoilerLogCheck = tk.Checkbutton(frame, text="Generate Spoiler Log", variable=generateSpoilerLog, command=spoilerField)



openROMButton.grid(column=0, row=0)
seedEntryLabel.grid(column=1, row=0)
seedEntryBox.grid(column=2, row=0)
generateSeedButton.grid(column=3, row=0)

quickEscapeStartCheck.grid(column=0, row=1, padx=0)
generateSpoilerLogCheck.grid(column=2, row=1, padx=0)





root.mainloop()