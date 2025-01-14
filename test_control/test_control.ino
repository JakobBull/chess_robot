#include <SoftwareSerial.h>

// Define the SoftwareSerial pins
const int rxPin = 10;  // RX pin for SoftwareSerial
const int txPin = 11;  // TX pin for SoftwareSerial

// Create a SoftwareSerial object
SoftwareSerial mySerial(rxPin, txPin);

void setup() {
  Serial.begin(9600);   // Initialize the Serial communication with the computer
  mySerial.begin(9600); // Initialize SoftwareSerial communication with the SSC-32u
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();
    mySerial.write(command);
  }
}
