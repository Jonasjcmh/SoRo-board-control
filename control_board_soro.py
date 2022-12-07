# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 19:30:39 2022

@author: joti
"""

"""
Spyder Editor

This is a temporary script file.
"""
import serial
import time


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



input1=b'01000000'
input2=200   #Type the variable value of time divided by 10   2000 ms => 200
command=transf_command(input1, input2)



data=bytes.fromhex(command)
ser.write(data)


s = ser.read(size=4)
print(len(s))
int_val = int.from_bytes(s[1:3], "big")
volt=int_val/1000
string = s.hex()
print(string)
print(int_val)
print(volt)

print("Start: Before sleep")
time.sleep(1.8)
print("End: After sleep")



input1=b'00000010'
input2=200   #Type the variable value of time divided by 10   2000 ms => 200
command=transf_command(input1, input2)


data=bytes.fromhex(command)
ser.write(data)
s = ser.read(size=4)
print(len(s))
int_val = int.from_bytes(s[1:3], "big")
volt=int_val/1000
string = s.hex()
print(string)
print(int_val)
print(volt)





ser.close()
