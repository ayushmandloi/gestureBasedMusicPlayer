from pygame import mixer
import time
import serial
ser = serial.Serial('com8', 9600)
mixer.init()
mixer.music.load('E:\honey\All songs\New songs 2013\[Songs.PK] Bhaag Milkha Bhaag - 04 - Maston Ka Jhund.mp3')
mixer.music.play()
while True:
    x=ser.readline()
    print(x)
    y=float(x)
    mixer.music.set_volume(y)
