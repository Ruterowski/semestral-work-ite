#include <WiFi.h>
#include <WebServer.h>

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

  // Set the Wifi mode to access point
  WiFi.mode(WIFI_AP);
  // Pass in the ssid and password for the Wifi module
  WiFi.softAP(ssid, password);

  Serial.println("Access point ready");
  // Get the IP address
  IPAddress IP = WiFi.softAPIP();
  Serial.print("IP address: ");
  Serial.println(IP);

  // Start the WebServer
  server.begin();
  // Setup endpoint - base root endpoint
  server.on("/", ConnectionEstablished);
  Serial.println("WebServer started");
}

void loop() {
  // Run the server
  server.handleClient();
}
