import socket

server_ip= '127.0.0.1'
server_port =12345

# Creamos un socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Pedimos añ usuario que ingrese un mensaje 
    message = input("Ingrese un mensaje para enviar al servidor: ")

    # Enviamos el mensaje al servidor
    client_socket.sendto(message.encode(), (server_ip, server_port))

    # Esperamos la respuesta del servidor 
    response, server_address= client_socket.recvfrom(1024)
    print(f"Respuesta deñ servidor: {response.decode()}")

# Cerramos el socket
client_socket.close() 