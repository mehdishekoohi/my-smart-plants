const int dry = 510; // value for dry sensor
const int wet = 200; // value for wet sensor

void setup()
{ 
  Serial.begin(9600);
}

void loop()
{
  int sensorVal0 = analogRead(A0);
  int sensorVal1 = analogRead(A1);

  // Sensor has a range of 239 to 595
  // We want to translate this to a scale or 0% to 100%
  // More info: https://www.arduino.cc/reference/en/language/functions/math/map/
  int percentageHumididy0 = map(sensorVal0, wet, dry, 100, 0); 
  int percentageHumididy1 = map(sensorVal1, wet, dry, 100, 0); 

  Serial.print(sensorVal0);
  Serial.print(",");
  Serial.println(sensorVal1);
  
  
  delay(500);
}
