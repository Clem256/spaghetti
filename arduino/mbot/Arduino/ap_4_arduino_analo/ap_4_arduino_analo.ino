int consigne;
int const poten=A3;
int const vitesse=9;
void setup() {
  pinMode(vitesse,OUTPUT);
  Serial.begin(9600);

}
void loop() {
  consigne=analogRead(poten);
  Serial.println(consigne);
  analogWrite(vitesse,consigne/ 4);
  delay(200);
}
