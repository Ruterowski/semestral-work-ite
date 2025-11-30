import requests

class TestGreenLed:
    """
    Test class for green led.
    """
    def test_switch_led_green_on(self):
        """
        Test, switch green LED on.
        """
        response = requests.get(f"http://192.168.4.1/ledon?clr=green")
        assert response.status_code == 200
        assert response.text == "Green LED switched on"

    def test_switch_led_green_is_switched_on_already(self):
        """
        Test, green LED is already switched on.
        """
        response = requests.get(f"http://192.168.4.1/ledon?clr=green")
        assert response.text == "Green LED is already switched on"
        assert response.status_code ==  400

    def test_switch_led_green_off(self):
        """
        Test, switch green LED off.
        """
        response = requests.get(f"http://192.168.4.1/ledoff?clr=green")
        assert response.text == "Green LED switched off"
        assert response.status_code == 200

    def test_switch_led_green_off_already(self):
        """
        Test, green LED is already switched off.
        """
        response = requests.get(f"http://192.168.4.1/ledoff?clr=green")
        assert response.text == "Green LED is already switched off"
        assert response.status_code == 400
