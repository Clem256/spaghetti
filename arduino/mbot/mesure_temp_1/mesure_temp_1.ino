#include <Servo.h>
#include <math.h>
const int B = 4275;
const int R0 = 100000;
const int temp = A0;
int angle;
Servo toto ;
void setup() {
  toto.attach(7) ;
  Serial.begin(9600);
}

void loop() {
   int a = analogRead(temp);

   float R = 1023.0/a-1.0;
   R = R0 * R;

   float temperature  = 1.0/(log(R/R0)/B+1/298.15)-273.15;

   Serial.print("température =");
   Serial.println(temperature);
   angle = temperature * (-180 / 15 )+420 ;
   toto.write(angle);
   Serial.println(angle);

   delay(1000);
}
