from time import sleep
from threading import Thread
#Para hacer una recursión infinita, no puede ser de pila
#se prefiere recursión simple

def ejemplo1(i):
    print(i)
    i+=1
    sleep(0.001)
    #la llamada no se hace de manera directa, si no que usa un hilo
    Thread(target=ejemplo1, args =(i+1,)).start()

Thread(target=ejemplo1, args =(0,)).start()

