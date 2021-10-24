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

  delay(1000);
}
