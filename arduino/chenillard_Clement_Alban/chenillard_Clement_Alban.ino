const int LV=10;
const int LR=12;
const int LO=11;
const int B=2;
const int P=A0;
int pos;
int tempo;
int resultat;
void setup() {
  pinMode(LV,OUTPUT);
  pinMode(LR,OUTPUT);
  pinMode(LO,OUTPUT);
  pinMode(P,INPUT);
  pinMode(B,INPUT);

}

void loop() {
    digitalWrite(LR,0);
    digitalWrite(LV,1);
    tempo=calcul();
    delay(tempo);
    digitalWrite(LV,0);
    digitalWrite(LO,1);
    tempo=calcul();
    delay(tempo);
    digitalWrite(LO,0);
    digitalWrite(LR,1);
    tempo=calcul();
    delay(tempo);
}
int calcul(){
  pos=analogRead(P);
  resultat = (pos*2);
  return resultat;
  }
