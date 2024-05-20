void setup()
{
	Serial.begin(9600);
}

void loop()
{
	int val[8] = {0};
	char buff[50];
	Serial.print("Sensor Data: ");
	for (int i=0;i<8;i++)
	{
		val[i] = analogRead(i);
		sprintf(buff, "sens_%d=%d,",i,val[i]);
		Serial.print(buff);
	}
	Serial.println();
	delay(50);
}
