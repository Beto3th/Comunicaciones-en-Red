import socket 
import threading 

def recibir_mensajes(socket_cliente):
    while True:
        try:
            mensaje = socket_cliente.recv(1024).decode('utf-8')
            print(mensaje)
        except:
            print("Ha ocurrido un error. Saliendo del Chat")
            socket_cliente.close()
            break

def enviar_mensaje(socket_cliente):
    while True:
        mensaje = input()
        socket_cliente.send(bytes(mensaje, 'utf-8'))

def main():
    host = '127.0.0.1' #Direccion IP local 
    puerto = 5555

    cliente_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    cliente_socket.connect((host, puerto))

    # Iniciar threads para recibir y enviar mensajes simultaneos
    thread_recibir = threading.Thread(target=recibir_mensajes, args=(cliente_socket,))
    thread_recibir.start()

    thread_enviar = threading.Thread(target=enviar_mensaje, args=(cliente_socket,))
    thread_enviar.start()

if __name__ == "__main__":
    main()

