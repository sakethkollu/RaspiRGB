import socket
from gpiozero import LED
# GPIO Setting Up
red = LED(17)
green = LED(22)
blue = LED(24)

# Create a Server Socket and wait for a client to connect
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 6666))
print ("UDPServer Waiting for client on port 6666")

# Define moving functions

def red_on():
    red.on()

def green_on():
    green.on()

def blue_on():
    blue.on()

def red_off():
    red.off()

def green_off():
    green.off()

def blue_off():
    blue.off()



options = {    "0" : red_on,
               "1" : red_off,
               "2" : green_on,
               "3" : green_off,
               "4" : blue_on,
               "5" : blue_off,
}

# Recive data from client and decide which function to call
while True:
    try:
        dataFromClient, address = server_socket.recvfrom(256)
        dataFromClient = dataFromClient.rstrip()
        print(dataFromClient)
        options[dataFromClient]()
    except Exception as e:
        print(e)
        print("Incorrect data recieved from client")