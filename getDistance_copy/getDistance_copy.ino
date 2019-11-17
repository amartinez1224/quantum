/*
 * getDistance
 *
 * Example of using SharpIR library to calculate the distance beetween the sensor and an obstacle
 *
 * Created by Giuseppe Masino, 15 June 2016
 *
 * -----------------------------------------------------------------------------------
 *
 * Things that you need:
 * - Arduino
 * - A Sharp IR Sensor
 *
 *
 * The circuit:
 * - Arduino 5V -> Sensor's pin 1 (Vcc)
 * - Arduino GND -> Sensor's pin 2 (GND)
 * - Arduino pin A0 -> Sensor's pin 3 (Output)
 *
 *
 * See the Sharp sensor datasheet for the pin reference, the pin configuration is the same for all models.
 * There is the datasheet for the model GP2Y0A41SK0F:
 *
 * http://www.robotstore.it/open2b/var/product-files/78.pdf
 *
 */

//import the library in the sketch
#include <SharpIR.h>

//Create a new instance of the library
//Call the sensor "sensor"
//The model of the sensor is "GP2YA41SK0F"
//The sensor output pin is attached to the pin A0
SharpIR sensor( SharpIR::GP2Y0A41SK0F, A0 );
double mean =0;
int l =0;
float n_data=1000;
int velocity=0;
float Masses[100][3];
float last_data[10];
int last_data_saved=0;
float gravity=9.8;
float k_hooke=10.0;
int la=0;
int request=0;
int longitud;
int latitud;
int size_queue=10;
float derivada[9];
void setup()
{
  Serial.begin( 9600 ); //Enable the serial comunication
  for(int i = 0; i < 100; i++){

    for(int j = 0; j < 3; j++){

      Masses[i][j]=0;

    }//close for j

  }//close for i
}

void loop()
{ latitud=random(1,100);
  longitud=random(1,100);
  while (Serial.available()) {
  char inChar = (char)Serial.read();
  switch(inChar) {
      case '1':
      Serial.println("SYK634");
      for(int i = 0; i < 100; i++){
      Serial.print(";");
      Serial.print( Masses[i][0]);
      Serial.print(";");
      Serial.print( Masses[i][1]);
      Serial.print(";");
      Serial.println( Masses[i][2]);
      if ( Masses[i+1][0]==0 and Masses[i+1][1]==0){
      Serial.println("end");
        break;
      
      }

    }//close for i
    }
    break;
  }
  if (velocity==0){
  double Voltage=analogRead(A0);
  float Distance_new = 2.54*1208 * pow(Voltage , -1.058);
  mean =Distance_new+mean;
  l=l+1;
  if(l==n_data){
    if(la<size_queue){
    last_data[la]=mean/n_data;
    }
    else{
      pushq(mean/n_data);
    }
    if (la==size_queue){
      if (last_data_saved==0){
        Masses[0][0]=latitud;
        Masses[0][1]=longitud;
        Masses[0][2]=(mean/n_data)*(k_hooke/gravity);
        last_data_saved=last_data_saved+1;
        
      }
    }
    derivada_exc();
    int half=(int)(size_queue-1)/2;
    // and abs(derivada[half-1])<0.2 and abs(derivada[half-2])<0.2 and abs(derivada[half-3])<0.3 and abs(derivada[half+1])<0.4 and abs(derivada[half+2])<0.4
    if (abs(derivada[half])>0.3){
      Masses[last_data_saved][0]=latitud;
      Masses[last_data_saved][1]=longitud;
      Masses[last_data_saved][2]=(mean/n_data)*(k_hooke/gravity);
      last_data_saved=last_data_saved+1;
    }
    
    mean=0;
    l=0;
    la=la+1;
  }
  }
}

void pushq(float data){
  for(int p = 0; p < size_queue-1; p++){
    last_data[p]=last_data[p+1];
    }//close for p
  last_data[size_queue-1]=data;
}

void derivada_exc(){
  for(int g = 0; g < size_queue-2; g++){
    derivada[g]=last_data[g+1]-last_data[g];
    }//close for p
}
