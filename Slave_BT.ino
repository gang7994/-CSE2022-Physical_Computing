//Physical Computing Project
//소프트웨어학부 2018044857 이강영
#include <SoftwareSerial.h>

SoftwareSerial mySerial(2, 3); //Tx, Rx핀을 2번 3번핀으로 설정

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ; //시리얼통신이 연결되지 않았다면 코드 실행을 멈추고 무한 반복
  }
  Serial.println("Hello World!");
  mySerial.begin(9600);
}

void loop() { //코드를 무한반복
  if (mySerial.available()) { //블루투스에서 넘어온 데이터가 있다면
    Serial.write(mySerial.read()); //시리얼모니터에 데이터를 출력
  }
}
