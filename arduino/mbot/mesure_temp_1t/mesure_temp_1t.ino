#include <Adafruit_NeoPixel.h>
#include <Servo.h>
#include <math.h>
#ifdef __AVR__
#include <avr/power.h>
#endif
#define PIN            6
#define NUMPIXELS      10
Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
const int B = 4275;
//const int R0 = 100000;
const int temp = A0;
Servo toto ;

void setup() {
  toto.attach(7) ;
  pixels.setBrightness(255);
  pixels.begin();
  Serial.begin(9600);
}

void loop() {
  int a = analogRead(temp);
   for(int i = 0;i < NUMPIXELS;i++) {
    float R = 1023.0/a-1.0;
    R = R0 * R;
    float temperature  = 1.0/(log(R/R0)/B+1/298.15)-273.15;
    if (temperature < 20) {
      for(int a = 0;a <NUMPIXELS;a++){
        pixels.setPixelColor(i, pixels.Color(0,255,0));
     
        delay(200);
      }
      }
    if (temperature > 30) {
      for(int a = 0;a <NUMPIXELS;a++){
        pixels.setPixelColor(a, pixels.Color(255,0,0));
       
        delay(200);
      }
    }
    if (temperature < 30) {
      for(int b = 0;b <NUMPIXELS;b++){
         pixels.setPixelColor(b, pixels.Color(0,0,255));
     delay(200);
    }
     }
      Serial.println(temperature);
   }

   pixels.show();
}
