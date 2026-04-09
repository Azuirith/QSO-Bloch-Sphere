#define BAUD_RATE 9600

void setup()
{  
  Serial.begin(BAUD_RATE);
}

void loop() 
{
  if (Serial.available())
  {
    Serial.write(Serial.read());
  }
}