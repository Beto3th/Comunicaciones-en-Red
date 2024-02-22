import socket

# Definir el host y el puerto 
HOST = '127.0.0.1' #localhost
PORT = 65432

# Definir el nombre del archivo a enviar
file_name ='archivo_a_enviar.txt'

# Crear un socket TCP/ID
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Conectar al servidor
    s.connect((HOST, PORT))
    # ENVIAR EL NOMBRE DEL ARCHIVO
    s.sendall(file_name.encode())
    print("Enviando", file_name)
    # Abrir el archivo en modo lectura 
    with open(file_name, 'rb') as f:
        # Leer los datos del archivo y enviarlos al servidor
        data = f.read(1024)
        while data:
            s.sendall(data)
            data = f.read(1024)
    print('Archivo enviado exitosamente')
