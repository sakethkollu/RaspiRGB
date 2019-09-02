import socket
import pigpio
import json

pi = pigpio.pi()

pins = {"red" : 17, "green" : 22, "blue" : 24}

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

        pi.set_PWM_dutycycle(pins[color], power)

    except Exception as e:
        print(e)
        print("Incorrect data recieved from client")
