#algunos reemplazos para ejecuciones infinitas
from tkinter import *
from threading import Thread


root = Tk()

def ejemplo1(i):
    print(i)
    root.after(1,lambda : ejemplo1(i+1))
    #hilo se detiene solo al cerrar tkinter

#sin lambda
def ejemplo2(i):
    print(i)
    def recursion():
        nonlocal i
        ejemplo2(i+1)
    root.after(1,recursion)
    #hilo se detiene solo al cerrar tkinter


Thread(target=ejemplo1, args =(0,)).start()

root.mainloop()
