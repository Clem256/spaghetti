void setup() {
  pinMode(5,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(11,INPUT);
  pinMode(12,INPUT);
}

void loop() {
  
  if (digitalRead(11)==0&& digitalRead(12)==0) {
  digitalWrite(4,HIGH);
  analogWrite(5,85);
  digitalWrite(7,LOW);
  analogWrite(6,85);
  }
  
  else if (digitalRead(11)==1&&digitalRead(12)==1) {
  digitalWrite(4,LOW);
  analogWrite(5,0);
  digitalWrite(7,HIGH);
  analogWrite(6,0);
  }
  
   else if(digitalRead(11)==0&&digitalRead(12)==1) {
    digitalWrite(4,HIGH);
    analogWrite(5,85);
    digitalWrite(7,LOW);
    analogWrite(6,0);
  }
  
   else {
    digitalWrite(4,HIGH);
    analogWrite(5,0);
    digitalWrite(7,LOW);
    analogWrite(6,85);
    }
 }
    
  
