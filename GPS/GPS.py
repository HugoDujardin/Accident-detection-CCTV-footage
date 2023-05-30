#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO

import serial
import time

ser = serial.Serial('/dev/ttyS0',115200)
ser.flushInput()
time_count = 0

def send_at(command,back,timeout):
	global rec_buff2
	rec_buff =''
	ser.write((command+'\r\n').encode())
	time.sleep(timeout)
	if ser.inWaiting():
		time.sleep(0.01 )
		rec_buff = ser.read(ser.inWaiting())
		rec_buff2=rec_buff.decode()
	if rec_buff != '':
		if back not in rec_buff.decode():
			print(command + ' ERROR')
			print(command + ' back:\t' + rec_buff.decode())
			return 0
		else:
			print(rec_buff2)
			return 1
	else:
		print('GPS is not ready')
		return 0
		
		
print('Start GPS session...')
send_at("AT+CGPS=0","OK",1)
send_at('AT+CGPS=1,1','OK',1)
time.sleep(3)

while "ERROR" in rec_buff2:
	send_at("AT+CGPS=0","OK",1)
	send_at('AT+CGPS=1,1','OK',1)
	time.sleep(3)
	
send_at('AT+CGPSINFO','+CGPSINFO: ',1)
time.sleep(1.5)
while ',,,,,' in rec_buff2:
	send_at('AT+CGPSINFO','+CGPSINFO: ',1)
	time.sleep(1.5)
send_at("AT+CGPS=0","OK",1)

