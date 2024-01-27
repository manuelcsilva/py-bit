import serial

ser = serial.Serial('COM9', 115200)	#Configurando e abrindo a porta

print(ser.read())
