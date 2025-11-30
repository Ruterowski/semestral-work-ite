# Semestral Work Information Technology
## Purpose of the program
The main purpose of the program was to create a simple GUI in Python which allows the user to controll ESP32 microcontroller.
<br>As of current state of the project, the user is able to controll a small display on the ESP32 board itself and 3 connected LEDs (red, Green, Blue).
## Install Instructions
Clone the git repository using
```bash
git clone https://github.com/Ruterowski/semestral-work-ite.git
```
After that, navigate to the main Python folder in the repository.<br>
Before running the program, you need to install the required packages. Please do so by executing:
```bash
pip install -r requirements.txt
```
## Usage manual
Before running the Python script, make sure to connect the ESP32 to your PC. Open up ArduinoIDE, and upload the code, which is present in the "server" directory.
<br> The ESP32 should host a webserver. To verify that it has been hosted, check the display of the board. It should say "Web server started"
To run the Python program, make sure to connect your PC to the ESP32 Wifi. 
**Without that, it is impossible to run the program!**
<br>
<br>After installing the packages, to run the program, simply type
```bash
python main.py
```
You should see a GUI window pop-up. From this point, you can have fun using our product.
## Limitations/Known issues
- Currently, to use the Python program, user needs to be connected to Wifi hosted by ESP32.
- Implementing HTU21 temperature and humidity sensor makes the ESP32 board crash.
## Tests
[Tests Documentation](python/tests/tests.md)
