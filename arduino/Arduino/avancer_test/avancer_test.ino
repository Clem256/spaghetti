void setup() {
pinMode(4,OUTPUT);
pinMode(5,OUTPUT);
pinMode(6,OUTPUT);
pinMode(7,OUTPUT);

}

void loop() {
  digitalWrite(4,HIGH);
  analogWrite(5,127);
  digitalWrite(7,LOW);
  analogWrite(6,127);
  delay(2000);
  analogWrite(5,0);
  analogWrite(6,0);
  delay(2000);
  digitalWrite(4,LOW);
  analogWrite(5,127);
  digitalWrite(7,HIGH);
  analogWrite(6,127);
  delay(2000);
  analogWrite(5,0);
  analogWrite(6,0);
  
}
 
