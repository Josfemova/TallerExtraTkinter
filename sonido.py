import vlc_aux as ost
from tkinter import *

root = Tk()
root.minsize(600,200)
Canv = Canvas(root, width = 600, height = 400)
Canv.place(x=0,y=0)


btn_play = Button(Canv, text = "play", font=("Arial", 24), command=lambda:ost.reproducir_ost("./sample.mp3"))
btn_play.place(x=20, y=20)

btn_stop = Button(Canv, text = "stop", font=("Arial", 24), command=lambda:ost.detener_ost())
btn_stop.place(x=120, y=20)

btn_fx = Button(Canv, text = "fx", font=("Arial", 24), command=lambda:ost.reproducir_fx("./fx.mp3"))
btn_fx.place(x=300, y=20)

root.mainloop()