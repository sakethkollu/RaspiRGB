import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
IPADRESS = "192.168.1.14"
while 1:
    try:
        color = input("Enter Color : ").lower()
        power = input("Enter Power for " + color + " : ")
        data = (color, power)
        client_socket.sendto(data, (IPADRESS,6666))
        print ("Sending request")
    except Exception as ex:
        print(ex)

client_socket.close()