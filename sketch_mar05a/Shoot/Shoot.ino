int inPin = 6;
int inPinval = 0;

int outPin = 2;
int outPinval = 0;

int synchPin = 10;

int eventInput = 0;

void setup() {
  // put your setup code here, to run once:

Serial.begin(9600);

pinMode(LED_BUILTIN, OUTPUT);

pinMode(inPin, INPUT);
digitalWrite(inPin, HIGH);

pinMode(outPin, OUTPUT);
digitalWrite(outPin, LOW);

pinMode(synchPin, OUTPUT);
digitalWrite(synchPin, LOW);

}

void loop() {
  // put your main code here, to run repeatedly:

inPinval = digitalRead(inPin);
digitalWrite(LED_BUILTIN, inPinval);

outPinval = Serial.read();

  // to use switch as task response key
if (inPinval == LOW) Serial.write(45);


  //to trigger ds7a with serial input from task:
if (outPinval > 0) {
  if (outPinval == 2) {
    digitalWrite(outPin, HIGH);
    delay(50); 
    digitalWrite (outPin, LOW);
    delay(50);
  }
  else if (outPinval == 1) {
    digitalWrite(synchPin, HIGH);
    delay(50); 
    digitalWrite (synchPin, LOW);
    delay(50);
  }

}
}
