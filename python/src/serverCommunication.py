"""
Module, which holds the implementation of communication with the server
"""

import requests

led_states = {
    "green": False,
    "yellow": False,
    "red": False
}

def checkServerStatusConnection():
    """
    Method that pings the server.
    :returns response: Response object from the server with welcome message.
    """
    response = requests.get("http://192.168.4.1/")
    return response

def displayUserMessage(message):
    """
    Method that displays user's message on the display of ESP32.
    :param message: User's message.
    :return: Response object from the server.
    """
    response = requests.get(f"http://192.168.4.1/displayMessage?msg={message}")
    return response

def toggleLed(led_label, color):
    """
    Method that switches LEDs on or off.
    :param led_label: Label of the LED button
    :param color: Color of the LED
    :return: Response object from the server.
    """
    led_states[color] = not led_states[color]

    if led_states[color]:
        response = requests.get(f"http://192.168.4.1/ledon?clr={color}")
        led_label.config(text="OFF")
    else:
        response = requests.get(f"http://192.168.4.1/ledoff?clr={color}")
        led_label.config(text="ON")
    return response
