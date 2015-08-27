int incomingByte=0;
int fl1=0,fl2=0,fl3=0,mode=0;

void setup() {
  // put your setup code here, to run once:
  pinMode(42, INPUT); //right
  pinMode(40, INPUT); //up
  pinMode(38, INPUT); //down
  pinMode(36, INPUT); //left
  
  pinMode(52, OUTPUT);
  pinMode(50, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  Serial.begin(9600);
  motorStop();
}

void motorForward()
{
  digitalWrite(52,1);
  digitalWrite(50,0);
}

void motorBackward()
{
  digitalWrite(52,0);
  digitalWrite(50,1);
}

void motorStop()
{
  digitalWrite(52,0);
  digitalWrite(50,0);
  //char incomingByte = '0';
}

void loop() {
  if(digitalRead(42) == 0)
  {
    Serial.print('U');
  }
  if(digitalRead(40) == 0)
  {
    Serial.print('R');
  }
  if(digitalRead(38) == 0)
  {
    Serial.print('D');
  }
  if(digitalRead(36) == 0)
  {
    Serial.print('L');
  }
  //digitalWrite(39,1);
  if(Serial.available()>0)
  {
   incomingByte = Serial.read();
   //digitalWrite(ledpin,1);
   //delay(1000);
   //digitalWrite(ledpin,0);
   //delay(1000);
   
   /*if(incomingByte=='Q')
   {
    Serial.print(digitalRead(41));
    Serial.print(digitalRead(43));
    Serial.print(digitalRead(45));
    Serial.print(digitalRead(47));
    Serial.print(digitalRead(49));
    Serial.print(digitalRead(51));
    Serial.print(digitalRead(53));
    Serial.println("");
   }*/
   if(incomingByte=='M')
   {
    motorForward();
    delay(500);
    motorStop();
   }
   if(incomingByte=='R')
   {
    motorForward();
    delay(750);
    motorStop();
   }
   if(incomingByte=='K')
   {
    motorForward();
    delay(1000);
    motorStop();
   }
   if(incomingByte=='A')
   {
    mode = 1;
   }
   if(incomingByte=='B')
   {
      analogWrite(11, 0);
      analogWrite(12, 0);
      analogWrite(13, 0);
     mode = 0;
   }
  }
  if(mode == 1)
   {
      analogWrite(11, 255);
      analogWrite(12, 0);
      analogWrite(13, 0);
      delay(50);
      mode = 2;
   }
   else if(mode == 2)
   {
      analogWrite(11, 0);
      analogWrite(12, 255);
      analogWrite(13, 0);
      delay(50);
      mode = 3;
   }
   else if(mode == 3)
   {
      analogWrite(11, 0);
      analogWrite(12, 0);
      analogWrite(13, 255);
      delay(50);
      mode = 4;
   }
   else if(mode == 4)
   {
      analogWrite(11, 255);
      analogWrite(12, 255);
      analogWrite(13, 255);
      delay(50);
      mode = 1;
   }
}
