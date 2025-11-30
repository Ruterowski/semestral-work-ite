"""
Modul, which holds the implementation of creating the GUI window.
"""

import tkinter
from .serverCommunication import *

root = tkinter.Tk()

led_on = False

green_img = tkinter.PhotoImage(file="assets/led_images/green.png")
green_img = green_img.subsample(4, 4)
yellow_img = tkinter.PhotoImage(file="assets/led_images/yellow.png")
yellow_img = yellow_img.subsample(4, 4)
red_img = tkinter.PhotoImage(file="assets/led_images/red.png")
red_img = red_img.subsample(4, 4)

def startGui():
    """
    Main method for creating and running the GUI window.
    """
    root.geometry("1000x1000")
    root.title("ITE Semestral work")
    addMainLabel()
    addEntryForDisplayingUserMessage()
    addLedControlPannel()
    root.mainloop()

def addMainLabel():
    """
    Creates the main label with welcome message to the GUI.
    """
    label = tkinter.Label(root, text="Welcome to ITE Semestral Work Project", font=("Arial", 30))
    label.grid(row=0, column=0)
    response = checkServerStatusConnection()
    label_connection = tkinter.Label(root, text=response.text, font=("Arial", 20))
    label_connection.grid(row=1, column=0)

def addEntryForDisplayingUserMessage():
    """
    Creates a user entry field. Allows user to enter a message which will be displayed on the ESP32.
    """
    message_var = tkinter.StringVar()
    message_var.set("")

    label = tkinter.Label(root, text="Enter your message", font=("Arial", 20))
    label.grid(row=2, column=0)

    entry = tkinter.Entry(root, textvariable=message_var)
    entry.grid(row=3, column=0)

    button = tkinter.Button(root, text="Submit", command=lambda: displayUserMessage(message_var.get()))
    button.grid(row=4, column=0)

def addLedControlPannel():
    """
    Creates a LED control panel. Allows the user to switch on/off corresponding LED on ESP32.
    """
    frame = tkinter.Frame(root)
    frame.grid(row=5, column=0, columnspan=3)

    label_green = tkinter.Label(frame, image=green_img)
    label_yellow = tkinter.Label(frame, image=yellow_img)
    label_red = tkinter.Label(frame, image=red_img)

    label_green.grid(row=0, column=0, padx=10)
    label_yellow.grid(row=0, column=1, padx=10)
    label_red.grid(row=0, column=2, padx=10)

    button_green = tkinter.Button(frame, text="ON", command=lambda: toggleLed(button_green, "green"))
    button_green.grid(row=1, column=0)
    button_yellow = tkinter.Button(frame, text="ON", command=lambda: toggleLed(button_yellow, "yellow"))
    button_yellow.grid(row=1, column=1)
    button_red = tkinter.Button(frame, text="ON", command=lambda: toggleLed(button_red, "red"))
    button_red.grid(row=1, column=2)

