#include <Arduino.h>
#include <Servo.h>

int trig = 6;
int echo = 7;
long duration;
int distance;
int x;
int value;
Servo servo1;
int servoPin = 8;
int peebPin = 5;

void close_door()
{
  servo1.write(0);
  delay(1000);
}

void open_door()
{
  servo1.write(180);
  delay(1000);
}

void sensor_door_open()
{
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, LOW);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  duration = pulseIn(echo, LOW);
  digitalWrite(peebPin, LOW);
}

void alarm_open()
{
  for (int i = 0; i < 50; i++)
  {
    PORTB = PORTB ^ (1 << PB5);
    PORTB = PORTB ^ (1 << PB4);
    PORTB = PORTB ^ (1 << PB3);
    PORTB = PORTB ^ (1 << PB2);
    PORTB = PORTB ^ (1 << PB1);
    digitalWrite(peebPin, HIGH);
    delay(100);
    digitalWrite(peebPin, LOW);
    delay(100);
  }
}
void alarm_close()
{
  digitalWrite(peebPin, LOW);
  digitalWrite(13, LOW);
  digitalWrite(12, LOW);
  digitalWrite(11, LOW);
  digitalWrite(10, LOW);
  digitalWrite(9, LOW);
}

void setup()
{
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(peebPin, OUTPUT);
  servo1.attach(servoPin);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available() > 0)
  {
    String data = Serial.readStringUntil('\n');

    if (data.compareTo("LED_ON_VARDAGSRUM") == 0)
    {
      digitalWrite(13, HIGH);
    }
    if (data.compareTo("LED_OFF_VARDAGSRUM") == 0)
    {
      digitalWrite(13, LOW);
    }
    if (data.compareTo("LED_ON_RUM") == 0)
    {
      digitalWrite(12, HIGH);
    }
    if (data.compareTo("LED_OFF_RUM") == 0)
    {
      digitalWrite(12, LOW);
    }
    if (data.compareTo("LED_ON_BADRUM") == 0)
    {
      digitalWrite(11, HIGH);
    }
    if (data.compareTo("LED_OFF_BADRUM") == 0)
    {
      digitalWrite(11, LOW);
    }
    if (data.compareTo("LED_ON_KOK") == 0)
    {
      digitalWrite(10, HIGH);
    }
    if (data.compareTo("LED_OFF_KOK") == 0)
    {
      digitalWrite(10, LOW);
    }
    if (data.compareTo("LED_ON_HALL") == 0)
    {
      digitalWrite(9, HIGH);
    }
    if (data.compareTo("LED_OFF_HALL") == 0)
    {
      digitalWrite(9, LOW);
    }
    if (data.compareTo("LED_OFF_ALL") == 0)
    {
      digitalWrite(13, LOW);
      digitalWrite(12, LOW);
      digitalWrite(11, LOW);
      digitalWrite(10, LOW);
      digitalWrite(9, LOW);
    }
    if (data.compareTo("LED_ON_ALL") == 0)
    {
      digitalWrite(13, HIGH);
      digitalWrite(12, HIGH);
      digitalWrite(11, HIGH);
      digitalWrite(10, HIGH);
      digitalWrite(9, HIGH);
    }
    if (data.compareTo("OPEN_DOOR") == 0)
    {
      open_door();
      sensor_door_open();
    }
    if (data.compareTo("CLOSE_DOOR") == 0)
    {
      close_door();
    }
    if (data.compareTo("SAFE_MODE") == 0)
    {
      close_door();
      digitalWrite(trig, LOW);
      delayMicroseconds(2);
      digitalWrite(trig, HIGH);
      delayMicroseconds(10);
      digitalWrite(trig, LOW);
      duration = pulseIn(echo, HIGH);
      distance = duration * 0.034 / 2;
      if (distance < 20 && distance > 0)
      {
        alarm_open();
      }
    }
    if (data.compareTo("TURN_OFF_ALL_ALARM") == 0)
    {
      alarm_close();
      sensor_door_open();
    }
  }
}
