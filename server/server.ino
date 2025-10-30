#include <WiFi.h> // Library for Wifi
#include <WebServer.h> // Library for WebServer
#include <TFT_eSPI.h> // Library to display on ESP32
#include <SPI.h>

TFT_eSPI tft = TFT_eSPI(); // Object for display on ESP32

// SSID of Wifi access point
const char* ssid = "ESP32";
// Password of Wifi access point
const char* password = "StrongPassword123";

// WebServer object
WebServer server(80);

// Endpoint - base root endpoint
void ConnectionEstablished(){
  // Return 200 response with successfull connection string
  server.send(200, "text/plain", "Connection established");
}

void setup() {
  // Enable serial monitor for debugging purposes
  Serial.begin(9600);

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
  Serial.println("WebServer started");
  tft.println("WebServer started");
}

void loop() {
  // Run the server
  server.handleClient();
}
