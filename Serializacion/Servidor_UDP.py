import socket

server_ip= '127.0.0.1'
server_port =12345

# Creamos un socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Ligamos el socket a la direccion IP y l puerto del servisopr
server_socket.bind((server_ip, server_port))

print("Servidor UDP iniciado")

while True:
    # Recibimos el mensaje del cliente y su direccion
    message, client_address = server_socket.recvfrom(1024)
    print(f"Mensaje recibido del cliente {client_address}: {message.decode()}")

    # Enviamos una respuesta al cliente 
    response ="Mensaje al cliente"
    server_socket.sendto(response.encode(), client_address)

# Cerramos el socket
server_socket.close()