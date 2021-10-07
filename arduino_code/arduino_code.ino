const int dry = 600; // value for dry sensor
const int wet = 250; // value for wet sensor

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  int sensorVal0 = analogRead(A0);
  int sensorVal1 = analogRead(A1);
  int sensorVal2 = analogRead(A2);
  int sensorVal3 = analogRead(A3);
  int sensorVal4 = analogRead(A4);

  // Sensor has a range of 239 to 595
  // We want to translate this to a scale or 0% to 100%
  // More info: https://www.arduino.cc/reference/en/language/functions/math/map/
  int percentageHumididy0 = map(sensorVal0, wet, dry, 100, 0);
  int percentageHumididy1 = map(sensorVal1, wet, dry, 100, 0);
  int percentageHumididy2 = map(sensorVal2, wet, dry, 100, 0);
  int percentageHumididy3 = map(sensorVal3, wet, dry, 100, 0);
  int percentageHumididy4 = map(sensorVal4, wet, dry, 100, 0);


  Serial.print("{'0': ");
  Serial.print(sensorVal0);
  Serial.print(",'1': ");
  Serial.print(sensorVal1);
  Serial.print(",'2': ");
  Serial.print(sensorVal2);
  Serial.print(",'3': ");
  Serial.print(sensorVal3);
  Serial.print(",'4': ");
  Serial.print(sensorVal4);
  Serial.println("}");


//  Serial.print("{'0': ");
//  Serial.print(percentageHumididy0);
//  Serial.print(",'1': ");
//  Serial.print(percentageHumididy1);
//  Serial.print(",'2': ");
//  Serial.print(percentageHumididy2);
//  Serial.print(",'3': ");
//  Serial.print(percentageHumididy3);
//  Serial.print(",'4': ");
//  Serial.print(percentageHumididy4);
//  Serial.println("}");

  delay(1000);
}
