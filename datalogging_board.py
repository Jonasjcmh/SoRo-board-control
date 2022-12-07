# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 20:35:50 2022

@author: joti
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 19:31:09 2022

@author: joti
"""

"""
Spyder Editor

This is a temporary script file.
"""
import serial
import time
import pandas as pd


first_info = {'item': ['0'],
'time': [0],
'pressure': [0] }
df = pd.DataFrame(first_info, columns = ['item', 'time', 'pressure'])





def transf_command(input_a1,input_a2):
    val1=int(input_a1, 2)
    val2=input_a2
    startc=0xFF
    endc=0xFE

    command= ((startc<<8) | val1 )
    command=((command<<8) | val2 )
    command=((command<<8) | endc )
    command_a2=hex(command)  #just for verification 
    command_a2=command_a2[2:]
    return command_a2
    





ser = serial.Serial(
    port='COM5',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

print(ser.isOpen())


to=time.perf_counter()


input1=b'01000000'
input2=200   #Type the variable value of time divided by 10   2000 ms => 200
command=transf_command(input1, input2)

data=bytes.fromhex(command)
ser.write(data)

i=0





while(i<=500):


    i=i+1
    
    s = ser.read(size=4)
    int_val = int.from_bytes(s[1:3], "big")
    volt=int_val/1000
    string = s.hex()
    i_time=time.perf_counter()-to
    print('count:    '+str(i)+'   time:  '+ str(i_time)  +  '         voltage:   '+str(volt))
    
    df2=pd.DataFrame([[i,i_time,volt]],columns = ['item', 'time', 'pressure'])
    df = df.append(df2,ignore_index =True)
    
       
    time.sleep(0.005)



input1=b'00000000'
input2=200   #Type the variable value of time divided by 10   2000 ms => 200
command=transf_command(input1, input2)
data=bytes.fromhex(command)
ser.write(data)

print(df)
df.to_csv(r'C:\Users\joti\Desktop\test.csv')
time.sleep(30)



ser.close()
