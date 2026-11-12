#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif
#define PIN            6
#define NUMPIXELS      10
Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
void setup() {
 pixels.setBrightness(255);
 pixels.begin();
 pinMode(3,INPUT);
}

void loop() {
 if(digitalRead(3)==1){
  for (int g = 0; g <= 4; g++) {
   for (int i = 0; i < NUMPIXELS; i++) {
    pixels.setPixelColor(i, pixels.Color(150, 150, 150));
    pixels.show();
    delay(200); 
    }
    for (int i = 0; i < NUMPIXELS; i++) {
     pixels.setPixelColor(i, pixels.Color(0, 0, 0));
    pixels.show();
     }
    }
  }
}
  
