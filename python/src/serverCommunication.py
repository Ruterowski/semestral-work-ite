from http.client import responses

import requests

led_states = {
    "green": False,
    "yellow": False,
    "red": False
}

def checkServerStatusConnection():
    response = requests.get("http://192.168.4.1/")
    print(response.text)
    return response.text

def displayUserMessage(message):
    response = requests.get(f"http://192.168.4.1/displayMessage?msg={message}")
    print(response.text)

def toggleLed(led_label, color):
    led_states[color] = not led_states[color]

    if led_states[color]:
        response = requests.get(f"http://192.168.4.1/ledon?clr={color}")
        led_label.config(text="OFF")
    else:
        response = requests.get(f"http://192.168.4.1/ledoff?clr={color}")
        led_label.config(text="ON")
    print(response.text)
