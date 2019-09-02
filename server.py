import RPi.GPIO as GPIO
import socket
import json
from time import sleep
GPIO.setmode(GPIO.BCM)
pins = {"red" : 17, "green" : 22, "blue" : 24}

for pin in [17,22,24]:
    GPIO.setup(pin, GPIO.OUT)

red = GPIO.PWM(17, 100)
green = GPIO.PWM(22, 100)
blue = GPIO.PWM(24, 100)

red.start(0)
green.start(0)
blue.start(0)

# Create a Server Socket and wait for a client to connect
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 6666))
print ("UDPServer Waiting for client on port 6666")

# Recive data from client and decide which function to call
while True:
    try:
        dataFromClient, address = server_socket.recvfrom(256)
        dataFromClient = dataFromClient.rstrip()
        
        data = json.loads(dataFromClient)
        
        color = data["color"]
        power = data["power"]

        if color.equals("red"):
            red.ChangeDutyCycle(power)
            sleep(0.01)
        if color.equals("green"):
            green.ChangeDutyCycle(power)
            sleep(0.01)
        if color.equals("blue"):
            blue.ChangeDutyCycle(power)
            sleep(0.01)
        

    except Exception as e:
        print(e)
        print("Incorrect data recieved from client")

red.stop()      # Stop the PWM
green.stop()  
blue.stop()  
GPIO.cleanup()  # Make all the output pins LOW
