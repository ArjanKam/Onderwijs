bool ledState = false; //De huidige status van de led

void setup() 
{
  Serial.begin(9600); // baud rate is 9600
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, ledState);
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
