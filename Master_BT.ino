//Physical Computing Project
//소프트웨어학부 2018044857 이강
#include <SoftwareSerial.h>

SoftwareSerial BTSerial(2, 3);
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);//PC에 결과를 출력
  BTSerial.begin(9600);
  BTS영erial.print("sdsdsd");
}

void loop() {
  // put your main code here, to run repeatedly:
  
  int sensor0 = analogRead(A0);
  int sensor1 = analogRead(A1);
  int sensor2 = analogRead(A2);
  /*
  Serial.print("0 : ");
  Serial.print(sensor0);
  Serial.print(" 1 : ");
  Serial.print(sensor1);
  Serial.print(" 2 : ");
  Serial.println(sensor2);
  */
  if(sensor0 > 500 && sensor1 < 500 && sensor2 < 500){
      Serial.println("도");
      Serial.println(0);
      BTSerial.println(0);
  }
  else if(sensor0 < 500 && sensor1 > 500 && sensor2 < 500){
      Serial.println("레");
      Serial.println(1);
      BTSerial.println(1);
  }
  else if(sensor0 < 500 && sensor1 < 500 && sensor2 > 500){
      Serial.println("미");
      Serial.println(2);
      BTSerial.println(2);
  }
  else if(sensor0 > 500 && sensor1 > 500 && sensor2 < 500){
      Serial.println("파");
      Serial.println(3);
      BTSerial.println(3);
  }else if(sensor0 < 500 && sensor1 > 500 && sensor2 > 500){
      Serial.println("솔");
      Serial.println(4);
      BTSerial.println(4);
  }
  else if(sensor0 > 500 && sensor1 < 500 && sensor2 > 500){
      Serial.println("라");
      Serial.println(5);
      BTSerial.println(5);
  }else if(sensor0 > 500 && sensor1 > 500 && sensor2 > 500){
      Serial.println("시");
      Serial.println(6);
      BTSerial.println(6);
  }
  else {
      Serial.println(7);
      BTSerial.println(7);
  }
  delay(500);


  
}
