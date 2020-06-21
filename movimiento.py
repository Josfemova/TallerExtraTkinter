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
root.minsize(800,600)
root.title('movimiento')
Canv = Canvas(root, width = 800, height = 600)
Canv.place(x=0,y=0)
#///////////////////////////////////////////
Canv.fondo = PhotoImage(file = 'img/bkg.png')

fondo1 = Canv.create_image(960,540, tags = ('f1'), image = Canv.fondo)
Canv.create_image(-960,540, tags = ('f2'), image = Canv.fondo)


def recursiveMov():
    coord = Canv.coords(fondo1)
    coord2 = Canv.coords('f2')
    if(coord[0] != (2880)):
        Canv.coords('f1', coord[0]+5, coord[1])
        Canv.coords('f2', coord2[0]+5, coord2[1])
    else:
        Canv.coords('f1', 960, coord[1])
        Canv.coords('f2', -960, coord2[1])
    if(OPEN == True):
        root.after(10, lambda: recursiveMov())

Thread(target =recursiveMov).start()

def close():
    global OPEN
    OPEN = False
    root.destroy()
    return
root.protocol("WM_DELETE_WINDOW", close)

root.mainloop()
