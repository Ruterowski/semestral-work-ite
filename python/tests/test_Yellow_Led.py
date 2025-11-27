import requests

class TestYellowLed():
    def test_switch_led_yellow_on(self):
        response = requests.get(f"http://192.168.4.1/ledon?clr=yellow")
        assert response.status_code == 200
        assert response.text == "Yellow LED switched on"

    def test_switch_led_yellow_is_switched_on_already(self):
        response = requests.get(f"http://192.168.4.1/ledon?clr=yellow")
        assert response.text == "Yellow LED is already switched on"
        assert response.status_code ==  400

    def test_switch_led_yellow_off(self):
        response = requests.get(f"http://192.168.4.1/ledoff?clr=yellow")
        assert response.text == "Yellow LED switched off"
        assert response.status_code == 200

    def test_switch_led_yellow_off_already(self):
        response = requests.get(f"http://192.168.4.1/ledoff?clr=yellow")
        assert response.text == "Yellow LED is already switched off"
        assert response.status_code == 400
