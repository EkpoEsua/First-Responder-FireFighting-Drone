//import the assisting libraries 
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

//define the ssid and the password
#ifndef STASSID
#define STASSID "KWS"
#define STAPSK  "raspberry"
#endif

//assign the ssid and the password to the a character array variable
const char* ssid     = STASSID;
const char* password = STAPSK;

//define connection variables as a character array
String ID = "01";
String AP_IP_addr = "192.168.4.1";
String port = "5000";
String sensorLatitude = "47.398039859999997";
String sensorLongitude = "8.5455725400000002";
String altitude = "2.00";
String slash = "/";

String request = String("http://" + AP_IP_addr + ":" + port + "/" + "sensor_data" + "/" + "sensorID_" + ID + "/" + "lat_" + sensorLatitude + "/" + "lon_" + sensorLongitude +"/"+"alt_"+altitude+"/"+"state_");

void setup() {
  //insert debug tests
  Serial.begin(115200);

  // ESP8266 takes a few moments to boot, so we give it a few seconds
  for(uint8_t t = 4; t > 0; t--) 
  {
    Serial.printf("[SETUP] WAIT %d...\n", t);
    Serial.flush();
    delay(1000);
  }

  // set the Sensor to be a WiFi client/station
  WiFi.mode(WIFI_STA);
  
  // Connect to the WiFi access point using it's information
  WiFi.begin(ssid, password);

  //wait for WiFi to connect
  while(WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }

  //set autoreconnection in the case of connection loss
  WiFi.setAutoReconnect(true);

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  // Set the senosor input pin to input
  pinMode(2, INPUT);

}

void loop() {
  //create a one second delay: in ms.
  delay(1000);

  //create instance of HTTPClient class
  HTTPClient http;
  
  // check if the WiFi is connected
  if(WiFi.status() == WL_CONNECTED) {
    
    // Check if pin 2 is HIGH
    if (digitalRead(2) == HIGH){
      //issue a GET request of the format:
      // /sensor_data/latitude/longitude/pinLevel
      // where latitude is the the sensor's latitude coordinate
      // longitude is the sensor's longitude coordinate
      // and pinLevel is the state of the pin connect to the fire sensor
      
      // Be sure to change this IP address and port number to match yours!!!
      http.begin(request+"HIGH");
      int httpCode = http.GET();
      http.end();
      Serial.println("Sent:");
      Serial.println(request+"HIGH");
    }
    
    else{
      // Be sure to change this IP address and port number to match yours!!!
      http.begin(request+"LOW");
      int httpCode = http.GET();
      http.end();
      Serial.println("Sent:");
      Serial.println(request+"HIGH");
    }
  }
  else{
    Serial.println("reconnecting...");
  }
}
