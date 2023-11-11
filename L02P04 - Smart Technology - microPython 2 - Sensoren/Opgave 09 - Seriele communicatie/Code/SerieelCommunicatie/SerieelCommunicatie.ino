bool ledState = true; //De huidige status van de led

void setup() 
{
  Serial.begin(9600); // baud rate is 9600
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() 
{ 
  if(Serial.read()== 't') 
  {
    digitalWrite(LED_BUILTIN, ledState);
    ledState=!ledState;
    Serial.print('m'); //schrijf 'm' naar UART
  } 
}

