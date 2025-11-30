from src.serverCommunication import *

class TestDisplay:
    """
    Test class for display.
    """
    def test_display_message_success(self):
        """
        Test, checking the successful message display
        """
        message = "test"
        result = displayUserMessage(message)
        assert result.text == f"Printed the message: {message}"
        assert result.status_code == 200

    def test_display_message_error(self):
        """
        Test, checking the error message display with no payload
        """
        response = requests.get("http://192.168.4.1/displayMessage")
        assert response.text == "Error: no message passed"
        assert response.status_code == 400