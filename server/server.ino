#include <WiFi.h>       // Library for Wifi
#include <WebServer.h>  // Library for WebServer
#include <TFT_eSPI.h>   // Library to display on ESP32
#include <SPI.h>

const int RedPin = 22; // variable to hold pin for red LED
const int YellowPin = 21; // variable to hold pin for yellow LED
const int GreenPin = 17; // variable to hold pin for green LED

TFT_eSPI tft = TFT_eSPI();  // Object for display on ESP32

// SSID of Wifi access point
const char* ssid = "ESP32";
// Password of Wifi access point
const char* password = "StrongPassword123";

// WebServer object
WebServer server(80);

// Endpoint - base root endpoint
void ConnectionEstablished() {
  // Return 200 response with successfull connection string
  server.send(200, "text/plain", "Connection established");
}

// Endpoint - display message
void DisplayMessage() {
  // Check if the payload contains the message
  if (server.hasArg("msg")) {
    String message = server.arg("msg");
    DisplayText(message);
    // Return 200 response with printed message
    server.send(200, "text/plain", "Printed the message: " + message);
  } else {
    // Return 400 reposnse with error message
    server.send(400, "text/plain", "Error: no message passed");
  }
}

//endpoint - Switch on the LEDs
void SwitchLedOn() {
  // Check if the payload contains the color
  if (server.hasArg("clr")) {
    String color = server.arg("clr");
    if (color == "red") {
      //Switch on red LED
      digitalWrite(RedPin, HIGH);
      //Return 200 response
      server.send(200, "text/plain", "Red LED switched on");
    } else if (color == "yellow") {
      //Switch on yellow LED
      digitalWrite(YellowPin, HIGH);
      //Return 200 response
      server.send(200, "text/plain", "Yellow LED switched on");
    } else if (color == "green") {
      //Switch on green LED
      digitalWrite(GreenPin, HIGH);
      //Return 200 response
      server.send(200, "text/plain", "Green LED switched on");
    }
    else {
      server.send(400, "text/plain", "Error: LED with that color doesn't exist");
    }
  } 
  else {
    //Return 400 response with error message
    server.send(400, "text/plain", "Error: no color argument provided");
  }
}

//endpoint - Switch off the LEDs
void SwitchLedOff() {
  //Check if the payload contains the color
  if (server.hasArg("clr")) {
    String color = server.arg("clr");
    if (color == "red") {
      //Switch off red LED
      digitalWrite(RedPin, LOW);
      //Return 200 response
      server.send(200, "text/plain", "Red LED switched off");
    } else if (color == "yellow") {
      //Switch off yellow LED
      digitalWrite(YellowPin, LOW);
      //Return 200 response
      server.send(200, "text/plain", "Yellow LED switched off");
    } else if (color == "green") {
      //Switch off green LED
      digitalWrite(GreenPin, LOW);
      //Return 200 response
      server.send(200, "text/plain", "Green LED switched off");
    } else {
      //Return 400 response with error message
      server.send(400, "text/plain", "Error: LED with that color doesn't exist");
    }
  } 
  else {
    server.send(400, "text/plain", "Error: no color argument provided");
  }
}

void setup() {
  // Enable serial monitor for debugging purposes
  Serial.begin(9600);

  pinMode(RedPin, OUTPUT);
  pinMode(YellowPin, OUTPUT);
  pinMode(GreenPin, OUTPUT);

  // Initialise the display
  tft.init();
  // Set the rotation to horizontal
  tft.setRotation(1);
  // Set the background color to black
  tft.fillScreen(TFT_BLACK);
  // Set the cursor at top left of the corner with font size 2
  tft.setCursor(0, 0, 2);
  // Set the text color to white
  tft.setTextColor(TFT_WHITE);
  // Set the Wifi mode to access point
  WiFi.mode(WIFI_AP);
  // Pass in the ssid and password for the Wifi module
  WiFi.softAP(ssid, password);

  Serial.println("Access point ready");
  tft.println("Acces point ready");
  // Get the IP address
  IPAddress IP = WiFi.softAPIP();
  Serial.print("IP address: ");
  Serial.println(IP);
  tft.print("IP address");
  tft.println(IP);

  // Start the WebServer
  server.begin();
  // Setup endpoint - base root endpoint
  server.on("/", ConnectionEstablished);
  // Setup endpoint - display message endpoint
  server.on("/displayMessage", DisplayMessage);
  //Setup endpoint - switch on LEDs
  server.on("/ledon", SwitchLedOn);
  //Setup endpoint - switch off LEDs
  server.on("/ledoff", SwitchLedOff);

  Serial.println("WebServer started");
  tft.println("WebServer started");
}

void loop() {
  // Run the server
  server.handleClient();
}

void DisplayText(String msg) {
  // Set the background color to black
  tft.fillScreen(TFT_BLACK);
  // Set the cursor at top left of the corner with font size 2
  tft.setCursor(0, 0, 2);
  tft.println(msg);
}