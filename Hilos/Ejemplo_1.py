import threading
import time
import logging

def contar_primos(n_primos, n_iter):
    logging.debug(f'Comienxo de ejecucion de {n_iter}')
    primos_encontrados = []
    valor_actual = 2
    while len(primos_encontrados) < n_primos:
        if es_primo(valor_actual):
            logging.debug(f'Primo encontrado por: {n_iter}')
            primos_encontrados.append(valor_actual)
        valor_actual += 1 
    
    logging.debug(f'Fin de la ejecucion de {n_iter}')
    return primos_encontrados

def ejecucion_en_hilos(iteraciones, n_primos):
    hilos = []
    for n in range(iteraciones):
        t = threading.Thread(target=contar_primos, args=(n_primos, n))
        hilos.append(t)
        t.start()
    for t in hilos:
        t.join()

def es_primo(n_primos):
    for i in range(2,n):
        if n_primos%i== 0:
            return False
    return True


def ejecucion_secuencial(iteraciones, numeros_primos):
    for i in range(iteraciones):

 


if __name__ == '__main__':
    numeros_primos == 2500
    for iteraciones in [1,4,10,20]:
        startt = time.time()
        ejecucion_secuencial(iteraciones, numeros_primos)
        logging.info(f'Secuencial - {iteraciones} iter: {time.time() - start:.4 }s')

        start = time.time()
        ejecucion_en_hilos(iteraciones, numeros_primos)
        logging.info(f'Threading - {iteraciones} iter: {time.time() - start:.4}s')