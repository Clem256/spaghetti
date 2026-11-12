void setup() {
  pinMode(11,INPUT);
  pinMode(13,OUTPUT);
  pinMode(12,INPUT);

}

void loop() {
  if ((digitalRead (11)==0)&&digitalRead(12)==0){
    digitalWrite(13,HIGH);

}
else{
  digitalWrite(13,LOW);
  }
  }
