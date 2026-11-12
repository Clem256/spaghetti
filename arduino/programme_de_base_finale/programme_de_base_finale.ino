#include <mesure_ultrason.h>
#include <Adafruit_NeoPixel.h>
Adafruit_NeoPixel pixels(2, 13, NEO_GRB + NEO_KHZ800);
float distance;              /*capteur ultrasonique a onde sonoriser (non) */
const int Md = 4;
const int vit_Md = 5;
const int Avd = 1;
const int Ard = 0;
const int Mg = 7;
const int vit_Mg = 6;
const int Avg = 0;
const int Arg = 1;
const int svlg = 11;        /* suiveur ligne */
const int svld = 12;
const int svlnoir = 0;
const int svlblanc = 1;
int toto=0;                  /* LEDS */
int i=0;
int p=0;
int temps=0;
int Duree;

void setup() {
  pixels.begin();
  Serial.begin(9600);  
  pinMode(3,OUTPUT);                  /*capteur ultrasonique a onde sonoriser (non) */
  pinMode(3,INPUT);  
  pinMode(4,OUTPUT);                  /* moteur */
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(11,INPUT);                /*suiveur*/
  pinMode(12,INPUT);
  pinMode(A7,INPUT);                  /*BP*/
  
}
void avancer(){
 digitalWrite(Md,Avd);
 analogWrite(vit_Md,170);
 digitalWrite(Mg,Avg);
 analogWrite(vit_Mg,170);
}

void tourner_droite(){
 digitalWrite(Md,Avd);
 analogWrite(vit_Md,0);
 digitalWrite(Mg,Avg);
 analogWrite(vit_Mg,255);
}
void tourner_gauche(){
 digitalWrite(Md,Avd);
 analogWrite(vit_Md,255);
 digitalWrite(Mg,Avg);
 analogWrite(vit_Mg,0);
 }
 void reculer(){
 digitalWrite(Md,Ard);
 analogWrite(vit_Md,130);
 digitalWrite(Mg,Arg);
 analogWrite(vit_Mg,130);
 }
void arret(){
 digitalWrite(Md,Avd);
 analogWrite(vit_Md,0);
 digitalWrite(Mg,Avg);
 analogWrite(vit_Mg,0);
 }
void contournement(){
  tourner_gauche(); 
  delay(650);
  avancer();
  delay(500);
  tourner_droite();
  delay(1000);
  avancer();
  delay(750);
  tourner_droite(); 
  delay(750);
  avancer();
  delay(100);
  tourner_gauche();
  delay(500);
  }
void loop() {
temps=millis();
if(temps<300){
avancer();
delay(310);
}
if(temps>12300){
  Serial.print("arret");
  if(digitalRead(svlg)==1 && digitalRead(svld)==0){
    avancer();
    delay(200);
    arret();
    delay(20000);
    }
  }
if(digitalRead(svlg)==0 && digitalRead(svld)==0){
  avancer();
  }
if(digitalRead(svlg)==1){
  tourner_droite();
  }
if(digitalRead(svld)==1){
  tourner_gauche();
  }
if(digitalRead(svlg)==1 && digitalRead(svld)==1){
  avancer();
  delay(500);
  tourner_droite();
  delay(400);
  avancer();
  delay(400);
  tourner_droite();
  delay(550);
  avancer();
  delay(250);
  }
}
