void setup() {
  pinMode(3,INPUT);
  pinMode(11,OUTPUT);
  pinMode(13,OUTPUT);
}

void loop() {
  if (digitalRead(3)==HIGH) {
     digitalWrite(11,LOW);
     digitalWrite(13,HIGH);
     delay(2000);
    digitalWrite(13,LOW);
    delay(2000);
}

  else {
    digitalWrite(11,HIGH);
}

}
