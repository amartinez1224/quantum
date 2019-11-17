import serial
import time
import numpy as np
import requests

# # Serial port parameters
serial_speed = 9600
serial_port = '/dev/tty.HC-06-SerialPort' # bluetooth shield hc-06

def RequestInfo():
    ser = serial.Serial(serial_port, serial_speed, timeout=1)
    b=bytes('1', 'utf-8')
    ser.write(b)
    data = ser.readline()
    Name=data.decode("utf-8")
    firstline=0
    lasti=0
    Datos=[]
    while(data.decode("utf-8")[0]!='e' ):
        if (data != ""):
            if(firstline):
                sub_datos=[]
                for i in range(1,len(data.decode("utf-8"))):
                    if (data.decode("utf-8")[i]==";"):
                        sub_datos.append(float(data.decode("utf-8")[lasti+1:i]))
                        lasti=i
                
                sub_datos.append(float(data.decode("utf-8")[lasti+1:]))
                Datos.append(sub_datos)
        else:
            print ("arduino doesnt respond")
        firstline=1
        data = ser.readline()
        lasti=0
    
    return(Name,np.array(Datos))

def makePost():
    # defining the api-endpoint
    API_ENDPOINT = "http://0.0.0.0:5000/postes"
    Name, Mass =RequestInfo()
    Mass[:,2]=10*Mass[:,2]
    Mass=Mass.astype(int)
    print(Mass)
    Mass=Mass.ravel()
    print(Mass)
    StrinMass=Mass.tobytes()
    # data to be sent to api
    data = {'Placa':Name,'Cambios': StrinMass}
    print(StrinMass)
    print(np.frombuffer(StrinMass, np.int))
    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, data = data)

    # extracting response text
    pastebin_url = r.text
    #print("The pastebin URL is:%s"%pastebin_url)


if __name__ == '__main__':
    Name,Mass=RequestInfo()
    makePost()
