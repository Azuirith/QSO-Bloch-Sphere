#define BAUD_RATE 9600

#define MESSAGE_SIZE 8
#define CONNECTION_REQUEST '1'

char inputBuffer[MESSAGE_SIZE];
char outputBuffer[MESSAGE_SIZE];

void setup()
{  
  Serial.begin(BAUD_RATE);
}

void loop() 
{ 
  outputBuffer[0] = CONNECTION_REQUEST;
  Serial.write(outputBuffer, MESSAGE_SIZE);

  while (!Serial.available()) {};

  while (Serial.availableForWrite())
  {
    Serial.write(outputBuffer, MESSAGE_SIZE);
  }
}