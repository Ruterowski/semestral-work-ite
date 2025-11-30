# Testing Documentation
## Testing approach
To ensure the main parts are working correctly, I have decided to write unit tests for getting data to the ESP32 board.
PyTest library has been used in order to achieve that. All tests are runnable via one Python script
```bash
python tests_main.py
```
**In order to run all tests, connect to the ESP32 Wifi** 
## Display test
Only 2 test cases are present.
- test_display_message_success - returns 200 response code with corresponding response text.
- test_display_message_error - returns 400, as the message field has not been passed in the payload
## Server connection tests
As the application works only on ESP32 Wifi, there is only 1 test case
- test_connect_to_server - returns 200 with welcoming message
## General LED tests
Those tests are for general LED testing, not color-tied
- test_switch_led_blue_does_not_exist - returns 400, as the blue LED does not exist in the system
- test_switch_on_no_color_passed - returns 400, the payload did not contain field with the color
- test_ switch_off_no_color_passed - returns 400, the payload did not contain field with the color
## Red/Green/Yellow LED tests
The tests for those 3 colors look the same.
- test_switch_led_(color)_on - returns 200, LED switched on
- test_switch_led_(color)_is_switched_on_already - returns 400, the LED is already switched on, cannot be switched on again
- test_switch_let_(color)_off - returns 200 , LED switched off
- test_switch_led_(color)_is_switched_off_already - returns 400, the LED is already switched off, cannot be swtiched off again

