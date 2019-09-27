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
String AP_IP_addr = "192.168.4.1";
String port = "5000";
String sensorLatitude = "lat_84.34";
String sensorLongitude = "lon_98.29";
String sensorAltitude = "alt_0.00";
String sensorID = "sensorID_01"

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
      http.begin("http://192.168.8.1:5000/sensor_data/sensorID_01/lat_29.3/lon_73.4/alt_0.00/state_HIGH");
//      http.begin("http://" + AP_IP_addr + ":" + port+ "/sensor_data/" + sensorLatitude + "/" + sensorLongitude + "/HIGH");
      int httpCode = http.GET();
      http.end();
      Serial.println("Sent:");
      Serial.println("http://" + AP_IP_addr + ":" + port+ "/sensor_data/" + sensorLatitude + "/" + sensorLongitude + "/HIGH");
    }
    
    else{
      // Be sure to change this IP address and port number to match yours!!!
      http.begin("http://192.168.8.1:5000/sensor_data/29.3/73.4/LOW");
      int httpCode = http.GET();
      http.end();
      Serial.println("Sent:");
      Serial.println("http://192.168.8.1:5000/sensor_data/29.3/73.4/LOW");
    }
  }
  else{
    Serial.println("reconnecting...");
  }
}
