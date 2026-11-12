int i=0;
int n=5;
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
   for (i=0;i<=4 ;i++) {
    for (n=5;n > 13; n=n+2){
      digitalWrite(n,1);
      delay(200);
   }
   digitalWrite(5,0);
   digitalWrite(7,0);
   digitalWrite(9,0);
   digitalWrite(11,0);
   digitalWrite(13,0);
    }
  }
}
