import socket
import json
import win32api
import wx
import numpy as np
from time import sleep

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
IPADRESS = "192.168.1.137"

 


app = wx.App(False) # the wx.App object must be created first.    
width, height = wx.GetDisplaySize()
'''
def getColorAndPower(x ,y):
    x_center = width / 2
    y_center = height / 2

    x, y = x - x_center, y_center - y
    
    r = (x **2 + y**2) ** 0.5
    r_scaled = r / min(width / 2, height / 2) * 100
    theta = np.arctan(y/x) * 180 / np.pi
    #print(r_scaled, theta)
    if(theta < 90 and theta > 30):
        color = "red"
    if(theta < 30 and theta > -30):
        color = "green"
    if(theta < -30 and theta > -90):
        color = "blue"

    if(r_scaled < 30):
        r_scaled = 0

    power = r_scaled
    print(color, power)
    return color, power


while 1:
    try:
        x, y = win32api.GetCursorPos()
        
        color, power = getColorAndPower(x, y)
        data = json.dumps({"color": color, "power": power }).encode('utf8')
        client_socket.sendto(data, (IPADRESS,6666))
        
        #print ("Sending request")
    except Exception as ex:
        print(ex)

'''

def sendData(color, power):
    data = json.dumps({"color": color, "power": power }).encode('utf8')
    client_socket.sendto(data, (IPADRESS,6666))

def setColor(R, G, B):
    sendData("red", R)
    sendData("green", G)
    sendData("blue", B)


while 1:
    try:
        
        setColor(0, 0, 255)
        
    except Exception as ex:
        print(ex)




client_socket.close()