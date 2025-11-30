import requests

class TestRedLed:
    """
    Test class for red led.
    """
    def test_switch_led_red_on(self):
        """
        Test, switch red LED on.
        """
        response = requests.get(f"http://192.168.4.1/ledon?clr=red")
        assert response.status_code == 200
        assert response.text == "Red LED switched on"

    def test_switch_led_red_is_switched_on_already(self):
        """
        Test, red LED already switched on.
        """
        response = requests.get(f"http://192.168.4.1/ledon?clr=red")
        assert response.text == "Red LED is already switched on"
        assert response.status_code ==  400

    def test_switch_led_red_off(self):
        """
        Test, switch red LED off.
        """
        response = requests.get(f"http://192.168.4.1/ledoff?clr=red")
        assert response.text == "Red LED switched off"
        assert response.status_code == 200

    def test_switch_led_red_off_already(self):
        """
        Test, red LED already switched off.
        """
        response = requests.get(f"http://192.168.4.1/ledoff?clr=red")
        assert response.text == "Red LED is already switched off"
        assert response.status_code == 400
