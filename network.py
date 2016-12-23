#!/usr/bin/python
import socket
import sys
import os
import string

s=socket.socket()
HOST="127.0.0.1" #address here
PORT=9758 #port goes here
MESSAGE = "Hello, World!"
if(s.connect((HOST,PORT)))!=0:
	while(True):
		data=s.recvfrom(1024)
		data2=str(data)
		data3=data2.split("x")
		i=1
		while(i<len(data3)):
			data4=data3[i].split("\\")
			j=0
			data5=data4[j].split(",")	
			data6=data5[j].split("'")
			data7=data6[j].split(",")
			data8=int(data7[j],16)
			print data8
			i=i+1
s.close()