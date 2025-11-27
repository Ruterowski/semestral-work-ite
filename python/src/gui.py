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
    root.geometry("1000x1000")
    root.title("ITE Semestral work")
    addMainLabel()
    addEntryForDisplayingUserMessage()
    addLedControlPannel()
    root.mainloop()

def addMainLabel():
    label = tkinter.Label(root, text="Welcome to ITE Semestral Work Project", font=("Arial", 30))
    label.grid(row=0, column=0)
    response = checkServerStatusConnection()
    label_connection = tkinter.Label(root, text=response.text, font=("Arial", 20))
    label_connection.grid(row=1, column=0)

def addEntryForDisplayingUserMessage():
    message_var = tkinter.StringVar()
    message_var.set("")

    label = tkinter.Label(root, text="Enter your message", font=("Arial", 20))
    label.grid(row=2, column=0)

    entry = tkinter.Entry(root, textvariable=message_var)
    entry.grid(row=3, column=0)

    button = tkinter.Button(root, text="Submit", command=lambda: displayUserMessage(message_var.get()))
    button.grid(row=4, column=0)

def addLedControlPannel():
    label_green = tkinter.Label(root, image=green_img)
    label_yellow = tkinter.Label(root, image=yellow_img)
    label_red = tkinter.Label(root, image=red_img)

    label_green.grid(row=5, column=0)
    label_yellow.grid(row=5, column=1)
    label_red.grid(row=5, column=2)

    button_green = tkinter.Button(root, text="ON", command=lambda: toggleLed(button_green, "green"))
    button_green.grid(row=6, column=0)
    button_yellow = tkinter.Button(root, text="ON", command=lambda: toggleLed(button_yellow, "yellow"))
    button_yellow.grid(row=6, column=1)
    button_red = tkinter.Button(root, text="ON", command=lambda: toggleLed(button_red, "red"))
    button_red.grid(row=6, column=2)
