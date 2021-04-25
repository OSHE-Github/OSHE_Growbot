#define LEDPIN 13
#define SENSORPIN 22
#define RELAYPIN 26

int sensorState = 0, lastState=0;

void setup() {
  // initialize the LED pin as an output:
  pinMode(LEDPIN, OUTPUT);
  pinMode(RELAYPIN, OUTPUT);
  // initialize the sensor pin as an input:
  pinMode(SENSORPIN, INPUT);
  digitalWrite(SENSORPIN, HIGH); // turn on the pullup
  
  Serial.begin(9600);
}

void loop() {
  // read the state of the pushbutton value:
  sensorState = digitalRead(SENSORPIN);

  // check if the sensor beam is broken
  // if it is, the sensorState is LOW:
  if (sensorState == LOW) {
    // turn LED on;
    digitalWrite(LEDPIN, HIGH);
    digitalWrite(RELAYPIN, HIGH);
    Serial.println("Broken");
  }
  else {
    // turn LED off:
    digitalWrite(LEDPIN, LOW);
    digitalWrite(RELAYPIN, LOW);
    Serial.println("Unbroken");
  }
}
