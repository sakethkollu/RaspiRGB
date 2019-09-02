import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1:
    try:
        data = input("Enter Data :")
        IPADRESS = "192.168.1.137"
        # 6666 = Number Port
        client_socket.sendto(data, (IPADRESS,6666))
        print ("Sending request")
    except Exception as ex:
        print(ex)
        break

client_socket.close()