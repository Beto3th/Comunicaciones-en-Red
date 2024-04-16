import socket 
import threading 

def recibir_mensajes(cliente_socket):
    while True:
        try:
            mensaje = cliente_socket.recv(1024).decode('utf-8')
            print(mensaje)
        except:
            print("Ha ocurrido un error. Saliendo del Chat")
            cliente_socket.close()
            break

def enviar_mensaje(cliente_socket):
    while True:
        mensaje = input()
        cliente_socket.send(bytes(mensaje, 'utf-8'))

def main():
    host = '127.0.0.1' #Direccion IP local 
    puerto = 5555

    servidor_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    servidor_socket.bind((host, puerto))
    servidor_socket.listen()

    print("El servidor esta escuchando en el puerto", puerto)

    cliente1, direccion1 = servidor_socket.accept()
    print("Cliente 1 conectado desde: ", direccion1)
    cliente1.send(bytes("Bienvenido al chat! Esperando al segundo cliente", 'utf-8'))
    
    cliente2, direccion2 = servidor_socket.accept()
    print("Cliente 2 conectado desde: ", direccion2)
    cliente2.send(bytes("Bienvenido al chat! Ya puedes comenzar a enviar mensajes", 'utf-8'))

    # Iniciar threads para recibir y enviar mensajes simultaneos
    thread_recibir1 = threading.Thread(target=recibir_mensajes, args=(cliente1,))
    thread_recibir1.start()

    thread_recibir2 = threading.Thread(target=recibir_mensajes, args=(cliente2,))
    thread_recibir2.start()

    thread_enviar1 = threading.Thread(target=enviar_mensaje, args=(cliente1,))
    thread_enviar1.start()

    thread_enviar2 = threading.Thread(target=enviar_mensaje, args=(cliente2,))
    thread_enviar2.start()

if __name__ == "__main__":
    main()

    