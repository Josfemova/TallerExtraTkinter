import glob
import os
from tkinter import *
import time
from threading import Thread


#------------Variables Globales-------------
OPEN = True
#///////////////////////////////////////////


#------------Inicio Tkinter-----------------
root=Tk()
root.minsize(600,200)
Canv = Canvas(root, width = 600, height = 400)
Canv.place(x=0,y=0)
#///////////////////////////////////////////


samusx = Canv.create_image(100,100, tags = ('samusx'))
samusy = Canv.create_image(300,100, tags = ('samusy'))

def cargarVariasImg(input, listaResultado):
    if(input == []):
        return listaResultado
    else:
        listaResultado.append(PhotoImage(file=input[0]))
        return cargarVariasImg(input[1:], listaResultado)


def cargarSprites(patron):
    x = glob.glob('img/sprites/'+patron)
    x.sort()
    return cargarVariasImg(x, [])

images = cargarSprites('samus*.png')



def recursiveAnimation(i):
    global images
    if(i==10):
        i=0
    if(OPEN==True):
        Canv.itemconfig('samusx', image = images[i])
        time.sleep(0.05)
        Thread(target =recursiveAnimation, args = (i+1,)).start()

def recursiveLambdaAnimation(i):
    global images
    if(i==10):
        i=0
    if(OPEN==True):
        Canv.itemconfig('samusy', image = images[i])
        root.after(50, lambda:recursiveLambdaAnimation(i+1))


#-----------Tareas Iniciales-------

#//////////////////////////////////

#----------Llamado de hilos-----------------------------------
Thread(target =recursiveAnimation, args = (0,)).start()
Thread(target =recursiveLambdaAnimation, args = (0,)).start()

#/////////////////////////////////////////////////////////////


def close():
    global OPEN
    OPEN = False
    root.destroy()
    return

root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()