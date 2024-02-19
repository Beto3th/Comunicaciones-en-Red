import socket

# Configuracion del cliente

HOST = '127.0.0.1' #Direccion IP del servidor
PORT = 65432        #Puerto del servidor

# Crear un socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Conectar al servidor
    s.connect((HOST,PORT))
    while True:
        # Enviar datos al servidor
        message = input("Ingrese un mensaje para enviar al servidor: ")
        s.sendall(message.encode())
        # Recibir respuesta del servidor
        data = s.recv(1024)
        print('Respuesta del servidor: ', data.decode())