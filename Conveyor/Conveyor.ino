#include "DCMotor.h"

// Maximun length for serial input.
const unsigned int MAX_INPUT_LENGTH = 10;

// Motor constants
DCMotor motor(16, 17, 4, false);
int power = 0;

void setup() {
  Serial.begin(115200);
  motor.stop();
}

// Converts serial input to integer in a non-blocking manner
void processByte(const byte input){
  static char inputLine[MAX_INPUT_LENGTH];
  static unsigned int index = 0;

  if(input == 'r'){
    return;
  }

  if(input == '\n'){
    inputLine[index] = 0;  
    index = 0;  
    power = atoi(inputLine);
  }

  if (index < MAX_INPUT_LENGTH - 1){
    inputLine[index++] = input;
  } 
} 

void loop(){
  if(!Serial.available()){
    return;
  }
  
  while(Serial.available()){
    int data = Serial.read();
    processByte(data);
  }

  motor.setPower(power);
}