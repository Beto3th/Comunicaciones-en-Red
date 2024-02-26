import threading
import time
import datetime
import logging

logging.basicConfig(level=logging.DEBUG, format= '[%(levelname)s] (%(threadName)-s) %(message)s')

def consultar(id_persona):
    logging.info("Consultando para el id " + str(id_persona))
    time.sleep(2)
    return

def guardar(id_persona, data):
    logging.info("Consultando para el id " + str(id_persona) + " data " + data)
    time.sleep(5)
    return


tiempo_ini = datetime.datetime.now()

t1=threading.Thread(name="hilo_1", target=consultar, args=(1, ))
t2=threading.Thread(name="hilo_2", target=guardar, args=(1, "SUPREME VICTORY" ))

# Invocar los hilos
t1.start()
t2.start()

# consultar(1)
# guardar(1, "pacman")

t1.join()
t2.join()

tiempo_fin = datetime.datetime.now()

print("Tiempo transcurrido " + str(tiempo_fin.second - tiempo_ini.second) + " segundos")

