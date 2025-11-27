import unittest
from src.serverCommunication import *

class TestDisplay():
    def test_display_message_success(self):
        message = "test"
        result = displayUserMessage(message)
        assert result.text == f"Printed the message: {message}"
        assert result.status_code == 200

    def test_display_message_error(self):
        response = requests.get("http://192.168.4.1/displayMessage")
        assert response.text == "Error: no message passed"
        assert response.status_code == 400