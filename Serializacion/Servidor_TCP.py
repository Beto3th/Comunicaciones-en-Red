import socket

# Definir el host y el puerto 
HOST = '10.1.141.42' #localhost
PORT = 65432

#Crear un socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #ENlazar el socket al host y puerto especificados
    s.bind((HOST, PORT))
    # Escuchar conexion entrantes
    s.listen()
    print("Esperando conexiones entrantes... ")
    conn,addr =s.accept()
    with conn:
        print("Conexion establecida con ", addr)
        # Recibir el nombre del archivo
        file_name=conn.recv(1024).decode()
        print("Recibiendo ", file_name)
        # Abrir el archivo en modo escritura binaria
        with open(file_name, 'wb') as f:
            #Recibir datos del cliente y escribirlos en el archivo
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)
        print('Archivo recibido exitosamente  ')
