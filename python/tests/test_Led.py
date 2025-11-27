import requests

class TestLed:
    def test_switch_led_blue_does_not_exist(self):
        response = requests.get(f"http://192.168.4.1/ledon?clr=blue")
        assert response.status_code == 400
        assert response.text == "Error: LED with that color doesn't exist"

    def test_switch_on_no_color_passed(self):
        response = requests.get(f"http://192.168.4.1/ledon")
        assert response.status_code == 400
        assert response.text == "Error: no color argument provided"

    def test_switch_off_no_color_passed(self):
        response = requests.get(f"http://192.168.4.1/ledoff")
        assert response.status_code == 400
        assert response.text == "Error: no color argument provided"