void setup() {
  pinMode(2,INPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(12,OUTPUT);
  Serial.begin(9600);
  


}


void loop() {
  if (digitalRead(2)==1)   {
    digitalWrite(10,HIGH);
    delay(2000);
    digitalWrite(10,0);
    digitalWrite(11,1);
    delay(1000);
    digitalWrite(11,0);
    digitalWrite(12,1);
    delay(5000);
    Serial.println( "passage autorisé");
    digitalWrite(12,0);
    
    
    
    }
   
    else {
   digitalWrite(11,1);
   delay(200);
   digitalWrite(11,0);
   delay(200); 
   Serial.println( "passageinterdit");

}
}
