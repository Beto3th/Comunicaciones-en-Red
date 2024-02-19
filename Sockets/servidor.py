import socket

# Configuracion del servidor

HOST = '127.0.0.1' #Direccion IP Local
PORT = 65432        #Puerto para escuchar


# Crear un socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Enlazar el socket y puerto especificado
    s.bind((HOST,PORT))
    # ESCUCHAR CONEXIONES ENTRANTES
    s.listen()
    print("Servidor escuchando en ", (HOST, PORT))
    # ACEPTAR CONEXIONES ENTRANTES
    conn, addr = s.accept()
    with conn:
        print("Conexion establecida desde ", addr)
        while True:
            # Recibir datos del cliente
            data = conn.recv(1024)
            if not data:
                break
            print("Mensaje recibido: ", data.decode())
            # Responder al cliente
            conn.sendall(b"Recibido: " + data)