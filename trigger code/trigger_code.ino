#define trigPin 9
#define echoPin 10
long duration;
int distance;
bool recording = false;  // Variable to track if the recording is active

void setup() {
  Serial.begin(9600);  // Start the serial communication
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');  // Read message from Python
    
    if (data == "BUSY") {
      recording = true;  // Video recording is active
    } else if (data == "DONE") {
      recording = false;  // Recording has ended
    }
  }

  if (!recording) {  // Only trigger when no recording is happening
    // Trigger and read the proximity sensor
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    
    duration = pulseIn(echoPin, HIGH); // Measure the time for echo
    distance = duration * 0.034 / 2;   // Convert to distance in cm

    if (distance < 2.5) {  // If the object is closer than 50 cm
      Serial.println("TRIGGER");  // Send trigger message
      delay(2000);                // Prevent repeated triggers
    }
    
    delay(500);  // Delay between each loop
  }
}
