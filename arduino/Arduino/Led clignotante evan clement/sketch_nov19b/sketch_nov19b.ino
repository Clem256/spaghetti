void setup() {
pinMode(2,INPUT);
pinMode(5,OUTPUT);
pinMode(7,OUTPUT);
pinMode(9,OUTPUT);
pinMode(11,OUTPUT);
pinMode(13,OUTPUT);
}

void loop() {
 if (digitalRead(2)==1){
   digitalWrite(5,1);
   delay(200);
   digitalWrite(7,1);
   delay(200);
   digitalWrite(9,1);
   delay(200);
   digitalWrite(11,1);
   delay(200);
   digitalWrite(13,1);
   delay(200);
   digitalWrite(5,0);
   digitalWrite(7,0);
   digitalWrite(9,0);
   digitalWrite(11,0);
   digitalWrite(13,0);
  }
}
